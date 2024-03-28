import torch

# 张量形状不同，仍可以按照元素操作
# 1. 适当复制，扩展元素，以便转换之后两个张量具有相同的形状
# 2. 执行元素操作
a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))
print(a)
print(b)
print(a + b)