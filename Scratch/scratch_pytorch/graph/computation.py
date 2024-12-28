import torch
import torch.nn.functional as F
y=torch.tensor([1.0])
x=torch.tensor([2])
w=torch.tensor([0.4])
b=torch.tensor([1])

z=w*x+b

output=torch.sigmoid(z)

print("output",output)

predicted_class=F.binary_cross_entropy(output,y)


print("predicted class",predicted_class)

logloss=-(y*torch.log(output)+(1-y)*torch.log(1-output))
print("logloss",logloss)