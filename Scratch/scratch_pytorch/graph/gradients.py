import torch
import torch.nn.functional as F
from torch.autograd import grad
y=torch.tensor([1.0])
x=torch.tensor([2])
w=torch.tensor([0.4],requires_grad=True)
b=torch.tensor([1.0],requires_grad=True)

z=w*x+b

output=torch.sigmoid(z)

print("output",output)

loss=F.binary_cross_entropy(output,y)
print("losss",loss)
loss.backward()

print("w.grad",w.grad)
print("b.grad",b.grad)
#https://chatgpt.com/share/676fa259-a964-800d-8416-7f9c37648e80


# logloss=-(y*torch.log(output)+(1-y)*torch.log(1-output))
# print("loss",logloss)