import torch

# 这也就是我们熟知的范数 L2范数
x = torch.tensor([3.0, 4.0])
print(torch.norm(x))

# L1范数，绝对值再求和
a = torch.abs(x).sum()
print(a)

# 矩阵的 Frobenius范数，类似与向量的L2范数
# 每个元素的平方之和开方运算
z = torch.arange(12,dtype=torch.float).reshape(3,-1)
print(torch.norm(z))