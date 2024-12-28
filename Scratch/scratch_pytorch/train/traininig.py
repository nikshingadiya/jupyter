import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
## Dataset
X_train=torch.tensor([
    [-1.2, 3.1],
    [-0.9, 2.9],
    [-0.5, 2.6],
    [2.3, -1.1],
    [2.7, -1.5]
])

y_train=torch.tensor([0.0,0.0,1.0,1.0,1.0])
y_test = torch.tensor([0, 1])
X_test=torch.tensor([
    [-0.8, 2.8],
    [2.6, -1.6]

])

class Toydataset(Dataset):
    def __init__(self,X,y):
        self.features = X
        self.labels = y
    def __getitem__(self,index):
        one_x=self.features[index]
        one_y=self.labels[index]
        return one_x,one_y
    def __len__(self):
        return self.labels.shape[0]

train_ds=Toydataset(X_train,y_train)
test_ds=Toydataset(X_test,y_test)


train_loader=DataLoader(dataset=train_ds,batch_size=2,shuffle=False,drop_last=True )
test_loader=DataLoader(dataset=test_ds,batch_size=2,shuffle=False)

## Neural Network
class NeuralNetwork(torch.nn.Module):
    def __init__(self,num_input,num_output):
        super().__init__()
        self.input=num_input
        self.output=num_output
        self.layers=torch.nn.Sequential(
                torch.nn.Linear(self.input,30),
                torch.nn.LeakyReLU(),
                torch.nn.Linear(30,20),
                torch.nn.Linear(20,self.output)
        )
    def forward(self,x):
        logits=self.layers(x)
        return logits


torch.manual_seed(123)
model=NeuralNetwork(2,2)

print("model",model)
optimizer=torch.optim.Adam(model.parameters(),lr=0.001)

num_epochs=3
for epoch in range(num_epochs):
    model.train()
    for batch_idx, (x_train,y_train_batch) in enumerate(train_loader):
        optimizer.zero_grad()
        output=model(x_train.float())
        loss=F.cross_entropy(output,y_train_batch.long())
        loss.backward()
        optimizer.step()
        print(f"Batch {batch_idx + 1}: ", loss.item())
        print(f"Epoch: {epoch + 1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train Loss {loss:.2f}")

    model.eval()

model.eval()

with torch.no_grad():
    out = torch.softmax(model(X_train.float()), dim=1)

torch.set_printoptions(sci_mode=False)
X_train_pred = torch.argmax(out, dim=1)
print("Probabilities: ")
print(X_train_pred, "\n")

print(X_train_pred == y_train.long())
print(torch.sum(X_train_pred == y_train))
    
def compute_accuracy(model, dataloader):

    model = model.eval()
    correct = 0.0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):

        with torch.no_grad():
            logits = model(features)

        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)
    
    return (correct / total_examples).item()

print("\n", compute_accuracy(model, test_loader))