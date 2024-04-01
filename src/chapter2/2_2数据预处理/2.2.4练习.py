import torch
import pandas as pd
import os

os.makedirs(os.path.join(".",'data'),exist_ok=True)
data_file = os.path.join(".",'data','data.csv')
with open("./data/data.csv", mode='w', encoding='utf') as f:
    f.write("name,age,phone\n")
    f.write("Ali,NA,15176\n")
    f.write("Bob,20,18710\n")
    f.write("Tom,19,13463\n")
    f.write("Jerry,NA,NA\n")
    f.write("Jenny,18,15842\n")
data = pd.read_csv(data_file)
# 处理缺失值
data = data.dropna(axis=1, thresh=(data.count().min() + 1))
print(data)

# 转化为张量格式
data = pd.get_dummies(data, dummy_na=True)
data_tensor = torch.tensor(data.to_numpy(dtype=float))

# 转化成功了，但是由于phone太大导致结果并不好
# 所以这可能就是为什么之前分成inputs 和 outputs
print(data_tensor)
