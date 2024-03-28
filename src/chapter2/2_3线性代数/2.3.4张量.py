import torch

# 张量是具有更多轴的数据结构，是具有任意数量轴的n维数组
x = torch.arange(24).reshape(2,3,4)
print(x)
