import torch

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
model=NeuralNetwork(50,3)
print('model',model)
num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print('trainble parameter',num_params)
print(model.layers[0].weight)
# print(len(model.layers[0].weight))
# print(model.layers[0].weight.shape)
# print(model.layers[0].bias)

X = torch.rand((1, 50))

with torch.no_grad():
    out = torch.softmax(model(X), dim=1)

print(out)