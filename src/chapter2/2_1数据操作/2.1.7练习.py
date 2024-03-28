import torch

x = torch.arange(12).reshape(3,4)
y = torch.tensor([
    [1,2,3,4],
    [4,3,2,1],
    [1,1,1,1]
])
# 练习1
print(x > y)

# 练习2 广播机制
a = torch.arange(6).reshape((2, 3, 1))
b = torch.arange(4).reshape((2, 1, 2))
print(a)
print(b)
print(a + b)
# 结论 增加维度3维：[]增多，数值会自增，arange范围要求 2*3=6,2*2=4