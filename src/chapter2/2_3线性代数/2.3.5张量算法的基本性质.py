import torch

x = torch.arange(20, dtype=torch.float32).reshape(5,4)
y = x.clone() # 分配新内存，x的副本
print(x)
print(x + y)

# 矩阵按元素乘法Hadamard product   不同于矩阵乘法！！！
print(x * y)

# 张量与标量运算，不改变形状
a = 2
print(a * x)
print(a + x)