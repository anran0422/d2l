from d2l import torch as d2l
from matplotlib import pyplot as plt
import numpy as np

# 1
def f(x):
    return x**3 - 1/x

x = np.arange(0.01, 3, 0.1) # 规避x的取值范围
# f(x) 以及f(x)在 x = 1 处的切线方程(需要用导数求，这该死的计算攻击我)
d2l.plot(x, [f(x), 4*x - 4], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
plt.show()