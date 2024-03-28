import pandas as pd
# 插值法和删除法
# 差值法
data = pd.read_csv("./data/house_tiny.csv") # 读取到数据
print(data)

# 处理缺失值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2] # 前两列，最后一列
# 只计算带有数字的列，并且原地替换
inputs.fillna(inputs.mean(numeric_only=True), inplace=True)
print(inputs)

# 类别值和离散值处理 dummy_na 是否显示NAN值
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)