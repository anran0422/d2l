import torch

x = torch.arange(4.0,requires_grad=True)
y = x * x
u = y.detach() # detach：分离
z = u * x

z.sum().backward()
print(x.grad == u) # tensor([True, True, True, True])

# 随后y上调用反向传播，得到导数
x.grad.zero_()
y.sum().backward()
print(x.grad == 2 * x) # tensor([True, True, True, True])