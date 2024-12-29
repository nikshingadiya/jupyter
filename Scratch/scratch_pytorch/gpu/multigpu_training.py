import torch
from torch.utils.data import Dataset, DataLoader, DistributedSampler
import torch.nn.functional as F
import torch.distributed as dist
import os

class NeuralNetwork(torch.nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Linear(num_inputs, 30),
            torch.nn.ReLU(),
            torch.nn.Linear(30, 20),
            torch.nn.ReLU(),
            torch.nn.Linear(20, num_outputs)
        )

    def forward(self, x):
        logits = self.layers(x)
        return logits


class ToyDataset(Dataset):
    def __init__(self, X, y):
        self.features = X
        self.labels = y

    def __getitem__(self, index):
        one_x = self.features[index]
        one_y = self.labels[index]
        return one_x, one_y

    def __len__(self):
        return self.labels.shape[0]


def prepare_dataset(rank, world_size):
    # Toy dataset (small for testing)
    X_train = torch.tensor([
        [-1.2, 3.1],
        [-0.9, 2.9],
        [-0.5, 2.6],
        [2.3, -1.1],
        [2.7, -1.5]
    ])
    y_train = torch.tensor([0, 0, 0, 1, 1])

    X_test = torch.tensor([
        [-0.8, 2.8],
        [2.6, -1.6],
    ])
    y_test = torch.tensor([0, 1])

    train_ds = ToyDataset(X_train, y_train)
    test_ds = ToyDataset(X_test, y_test)

    # Use DistributedSampler to split data across GPUs
    train_sampler = DistributedSampler(train_ds, num_replicas=world_size, rank=rank, drop_last=True)
    test_sampler = DistributedSampler(test_ds, num_replicas=world_size, rank=rank, shuffle=False)

    train_loader = DataLoader(
        dataset=train_ds,
        batch_size=2,
        sampler=train_sampler,
        pin_memory=True,
    )
    test_loader = DataLoader(
        dataset=test_ds,
        batch_size=2,
        sampler=test_sampler,
        pin_memory=True,
    )

    return train_loader, test_loader, train_sampler, test_sampler


def compute_accuracy(model, dataloader, device):
    model.eval()
    correct = 0.0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):
        features, labels = features.to(device), labels.to(device)

        with torch.no_grad():
            logits = model(features)
        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)
    return (correct / total_examples).item()


def main(rank, world_size, num_epochs):
    # Initialize process group for distributed training
    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)
    torch.manual_seed(123)

    # Set device for this process
    device = torch.device(f"cuda:{rank}")
    print(f"Rank {rank} using device {device}")

    # Prepare data
    train_loader, test_loader, train_sampler, test_sampler = prepare_dataset(rank, world_size)

    # Create and distribute the model
    model = NeuralNetwork(num_inputs=2, num_outputs=2).to(device)
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[rank])

    # Set up optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

    # Training loop
    for epoch in range(num_epochs):
        model.train()
        train_sampler.set_epoch(epoch)  # Ensure different shuffling across epochs

        for features, labels in train_loader:
            features, labels = features.to(device), labels.to(device)
            logits = model(features)
            loss = F.cross_entropy(logits, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Only print loss from rank 0
            if rank == 0:
                print(f"Epoch: {epoch+1:03d}/{num_epochs:03d} | "
                      f"Batchsize {labels.shape[0]:03d} | "
                      f"Train Loss: {loss:.2f}")

    # Compute accuracy after training
    if rank == 0:
        train_acc = compute_accuracy(model, train_loader, device=device)
        print(f"Training accuracy: {train_acc:.2f}")
        test_acc = compute_accuracy(model, test_loader, device=device)
        print(f"Test accuracy: {test_acc:.2f}")

    # Cleanup the process group
    dist.destroy_process_group()


if __name__ == "__main__":
    # Set the number of GPUs to use
    world_size = torch.cuda.device_count()

    # Ensure that environment variables for distributed training are set
    os.environ["MASTER_ADDR"] = "localhost"
    os.environ["MASTER_PORT"] = "12355"

    # Launch multiple processes, one per GPU
    torch.multiprocessing.spawn(
        main,
        args=(world_size, 3),  # world_size and num_epochs
        nprocs=world_size,
        join=True
    )
