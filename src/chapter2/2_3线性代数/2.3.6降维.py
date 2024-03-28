import torch

# 求和会降低维度
x = torch.arange(4,dtype=torch.float32)
print(x)
print(x.sum())

y = torch.arange(20).reshape(2,5,-1)
print(y)
y_sum_axis1 = y.sum(axis=1) # 将 2 5 -1 中的5这一维度删除了， -1实际上是2
print(y_sum_axis1)
print(y_sum_axis1.size()) # torch.Size([2, 2])
print(y_sum_axis1.shape) # torch.Size([2, 2])
print(y.sum(axis=[0,1])) # shape是属性， size是方法

# 平均值
print(x.mean())
print(x.sum() / x.numel())
z = torch.arange(6,dtype=torch.float32).reshape(2,3)
print(z)
print(z.mean(axis=0)) # 0轴的平均值
print(z.sum(axis=0) / z.shape[0])

# 非维度求和
A = torch.arange(4).reshape(-1,2)
sum_A = A.sum(axis=1, keepdim=True)
print(sum_A) # 求和之后保持了维度，除法进行了广播机制
print(sum_A.shape) # torch.Size([2,1])
print(A / sum_A) # 广播删除

#如果keepdim=False 广播机制还是可以进行，但是sum_A的维度就是1 torch.Size([2])

# 某个轴的累积总和
print(A.cumsum(axis=0))
print(A.cumsum(axis=1).shape) # torch.Size([2, 2])