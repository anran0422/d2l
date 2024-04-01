import torch

# 对非标量调用backward需要传入一个gradient参数，该参数指定微分函数关于self的梯度
# 只求偏导数的和，传入一个1梯度是合适的
x = torch.arange(4.0,requires_grad=True)
# x.grad.zero_() 之前没有计算过，所以不需要清0
y = x * x
# 等价于y.backward(torch.ones(len(x)))
y.sum().backward()
print(x.grad)