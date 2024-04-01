import torch

# 1. y = 2* x.T * x求导
x = torch.arange(4.0)
x.requires_grad_(True)
print(x.grad) # None

y = 2 * torch.dot(x, x)
print(y) # tensor(28., grad_fn=<MulBackward0>)
print(x.grad) # None
y.backward() # 反向传播函数计算y关于x每个分量的梯度
print(x.grad) # tensor([ 0.,  4.,  8., 12.])
print(x.grad == 4 * x)

print("-----------")

# 2. 清除梯度问题
x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad) # tensor([1., 1., 1., 1.])