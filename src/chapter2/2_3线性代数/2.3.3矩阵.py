import torch

x = torch.arange(20).reshape(5,-1)
y = x.T
print(y)

z = torch.tensor([
    [1,2,3],
    [2,4,5],
    [3,5,9]
])
print(z == z.T) #True