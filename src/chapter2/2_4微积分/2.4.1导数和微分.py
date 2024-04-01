import numpy as np
from d2l import torch as d2l
from matplotlib import pyplot as plt

def f(x):
    # return 2 * x - 3
    return 3* x**2 -4 * x

x = np.arange(0, 3, 0.1)
y = 2*x - 3
d2l.plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
plt.show()