import torch

# 这就是矩阵-向量积的拓展 不同于Hadamard
A = torch.arange(20, dtype=torch.float32).reshape(5,-1)
B = torch.arange(12,dtype=torch.float32).reshape(4,3)

C = torch.mm(A, B)
print(C)
print(C.shape)