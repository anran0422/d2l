import os
import pandas as pd

# 创建数据集并且读取

os.makedirs(os.path.join(".", "data"), exist_ok=True)
data_file = os.path.join(".", "data", "house_tiny.csv")
with open(data_file, "w") as f:
    f.write("NumRooms,ALley,Price\n") # 列名
    f.write("NA,Pave,127500.0\n")
    f.write("2.0,NA,106000.0\n")
    f.write("4.0,NA,178100.0\n")
    f.write("NA,NA,140000.0\n")

data = pd.read_csv(data_file) # 读取 对于不同的文件pd提供了很多读取方法
print(data)