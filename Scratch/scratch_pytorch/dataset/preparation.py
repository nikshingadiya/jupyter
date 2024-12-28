import torch
from torch.utils.data import Dataset, DataLoader

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
    [1.0,2.0],
    [-0.3,1.4]
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

for idx, (x, y) in enumerate(train_loader):
    print(f"Batch {idx + 1}: ", x, y)
    print()