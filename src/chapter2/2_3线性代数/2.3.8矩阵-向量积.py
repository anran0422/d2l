import torch

# 矩阵和一个向量的乘法   -> 矩阵和矩阵（多向量）的乘法

x = torch.arange(20,dtype=torch.float).reshape(5,4)
print(x)
A = torch.ones(4,dtype=torch.float)
print(x.shape) # torch.Size([5, 4])
print(A.shape) # torch.Size([4])

b = torch.mv(x, A)
print(b) # tensor([ 6., 22., 38., 54., 70.]) 默认是列向量！
print(b.shape) # torch.Size([5])