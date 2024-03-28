import torch

# x y + - * / ** exp等单元素运算
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x / y)
print(torch.exp(y))

# 张量连结
x = torch.arange(12, dtype=torch.float32).reshape(3,4)
y = torch.tensor([
    [2.0, 1, 4 ,3],
    [1, 2, 3, 4],
    [4, 3, 2, 1]
])
print(torch.cat((x,y), dim=0)) # 按0轴（行）拼接
print(torch.cat((x,y), dim=1)) # 按1轴（列）拼接

# 逻辑运算符构建二元张量
print(x == y)

# 对元素求和，产生单元素张量
print(x.sum())