import torch
from torch import linalg

print("-----1-----")
# 1.
A = torch.arange(1, 5).float()
res = A.T.T == A
print(res)
print("-----2-----")

# 2
B = torch.arange(2, 6).float()
res = A.T + B.T == (A + B).T
print(res)
print("-----3-----")

# 3
A = torch.arange(16,dtype=torch.float).reshape(4,4)
res = A + A.T == (A + A.T).T
print(res)
print("-----4-----")

# 4
x = torch.arange(24, dtype=torch.float).reshape(2, 3 ,4)
res = len(x) # 2 经过测试，len = shape[0]
print(len(x) == x.shape[0]) # True
print(res)
print("-----5-----")

# 5
x = torch.arange(24, dtype=torch.float)
print(len(x)) # 24
x = torch.arange(24, dtype=torch.float32).reshape(4,3,2,1)
print(len(x)) # 4
print("-----6-----")

# 6
A = torch.arange(12, dtype= torch.float).reshape(3, 4)
print(A)
print(A.sum(axis=1)) # 消灭列维度，就是列运算，剩下行
print(A / A.sum(axis=1, keepdim=True)) # False/不填 就会报错

# B = torch.arange(9, dtype=torch.float).reshape(3,3)
# print(B)
# print(B.sum(axis=1,keepdim=True))
# print(B / B.sum(axis=1, keepdim=True))
# print(B)
# print(B.sum(axis=1,keepdim=False))
# print(B / B.sum(axis=1, keepdim=False))
# print(B.sum(axis=1) == B.sum(axis=1,keepdim=True)) # 不完全相同
# print(B.sum(axis=1) == B.sum(axis=1,keepdim=True).T) # 竟然是转置的关系
print("-----7-----")

# 7
x = torch.arange(24,dtype=torch.float32).reshape(2,3,4)
print(x.sum(axis=0).shape) # 消掉该轴
print(x.sum(axis=1).shape)
print(x.sum(axis=2).shape)
print("-----8-----")

# 8
x = torch.rand(2,3,4,5)
y = torch.rand(2,3)
print(linalg.norm(x))
print(linalg.norm(y))