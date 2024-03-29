import torch

# 点积是个数
x = torch.arange(4,dtype=torch.float32)
y = torch.ones(4,dtype=torch.float32)
print(x)
print(y)

print(torch.dot(x,y)) # tensor(6.)

# 按元素乘法，再求和达到同样的效果
print(torch.sum(x * y)) # tensor(6.)