import numpy as np
import matplotlib

import matplotlib.pyplot as plt

#initial value problem
#y'=sin(x)   y(0)=0

step = 0.01
a_start = 0
b_start = 1
x_start = 0
y_start = 0

num_step = (b_start-x_start)/step
i = 0

x_values = []
y_values = []

#calc sin(x)

x_i = x_start
y_i = y_start
while i <= num_step:
    y_i = y_i + step*np.sin(x_i)
    x_i = x_i + step
    i = i+1
    print(y_i, x_i)
    x_values.append(x_i)
    y_values.append(y_i)



plt.plot(x_values, y_values)
plt.show()
