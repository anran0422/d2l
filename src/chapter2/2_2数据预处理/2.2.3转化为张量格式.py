import pandas as pd
import torch
data = pd.read_csv("./data/house_tiny.csv") # 读取到数据

# 处理缺失值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2] # 前两列，最后一列
inputs.fillna(inputs.mean(numeric_only=True), inplace=True)

# 类别值和离散值处理 dummy_na 是否显示NAN值
inputs = pd.get_dummies(inputs, dummy_na=True)

# 转化为张量格式
x = torch.tensor(inputs.to_numpy(dtype=float)) # True变为1
y = torch.tensor(outputs.to_numpy(dtype=float))
print(x)
print(y)
