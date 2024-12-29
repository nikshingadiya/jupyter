import torch
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

device=torch.device('mps' if torch.mps.is_available() else 'cpu')

print(device)

tensor_1 = torch.tensor([1., 2., 3.])
tensor_2 = torch.tensor([4., 5., 6.])
print(tensor_1 + tensor_2)