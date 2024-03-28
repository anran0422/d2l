import torch

# torch张量 和 numpy数组 共享低层内存，就地操作 更改一个张量另一个也会改变
x = torch.randn(5)
a = x.numpy()
b = torch.tensor(a)
print(type(a)) # <class 'numpy.ndarray'>
print(type(b)) # <class 'torch.Tensor'>

# 张量转化为python标量 item()
z = torch.tensor([3.5])
print(z, z.item(), float(z), int(z))