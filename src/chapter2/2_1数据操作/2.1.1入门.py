import torch

# 建立张量的方式
x = torch.arange(12)
y = torch.tensor([
    [1,2,3],
    [4,5,6]
])
# 查看张量形状
print(x.shape)
print(y.shape)
print(y.size())

# 计算元素个数
print(x.numel()) # 12
print(y.numel()) # 6

# 不改变元素数量和元素值，只改变形状
x = x.reshape(3,4)
print(x)
x = x.reshape(-1,6)
print(x)
x = x.reshape(6,-1)
print(x)

# 初始化特定张量
z = torch.zeros((3,3,4))
print(z)
z = torch.ones((3,3,4))
print(z)

# 从正太分布中随机采样，生成张量
z = torch.randn(3,4)
print(z)

# 嵌套包含数值的python列表，生成张量
z = torch.tensor([[1,2,3],[4,5,6]]) 
print(z)