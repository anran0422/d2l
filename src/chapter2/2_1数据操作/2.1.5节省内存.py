import torch

x = torch.randn(1,5)
y = torch.arange(5)
before = id(y)
before_x = id(x)
y = y + x
print(id(y) == before) # False 重新分配的内存
x += y
print(id(x) == before_x) # True

# 原地执行
z = torch.zeros_like(y) # 形状一样，数值为0
print(z)
print('id(z):', id(z)) # id(z): 1874968540272
z[:] = x + y
print('id(z):', id(z)) # id(z): 1874968540272
