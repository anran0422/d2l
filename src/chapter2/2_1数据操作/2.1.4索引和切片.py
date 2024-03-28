import torch

x = torch.arange(12).reshape(3,4)
print(x)

# 切片和索引
print(x[-1])
print(x[1:3])

# 修改单个元素
x[2,3] = 99
print(x)

# 修改多个元素
x[0:2, :] = -1
print(x)