import numpy as np
import matplotlib

import matplotlib.pyplot as plt

#initial value problem
#y'=sin(x)   y(0)=0

step = 0.5




a_start = 0
b_start = 10
x_start = 0
y_start = 0

num_step = (b_start-x_start)/step
i = 0

x_values_euler = []
y_values_euler = []
x_values_rk = []
y_values_rk = []
x_values_a = []
y_values_a = []


#calc sin(x)

x_i = x_start
y_i = y_start
#Euler numeric realization
while i <= num_step:
    y_i = y_i + step*np.sin(x_i)
    x_i = x_i + step
    i = i+1
    print(y_i, x_i)
    x_values_euler.append(x_i)
    y_values_euler.append(y_i)



a_start = 0
b_start = 10

x_start = 0
y_start = 0
i = 0
x_i = x_start
y_i = y_start




#Runge-Kutta
while i<= num_step:
    k_1 = np.sin(x_i)
    k_2 = np.sin(x_i + (step/2))
    k_3 = np.sin(x_i + (step/2))
    k_4 = np.sin(x_i+step)
    y_i = y_i + (step/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
    x_i = x_i + step
    print(y_i, x_i)
    x_values_rk.append(x_i)
    y_values_rk.append(y_i)
    i += 1
  



a_start = 0
b_start = 10

x_start = 0
y_start = 0
i = 0
x_i = x_start
y_i = y_start



step = 0.01
num_step = (b_start-x_start)/step
while i<= num_step:
    y_i = -np.cos(x_i) + 1
    print(y_i, x_i)
    x_values_a.append(x_i)
    y_values_a.append(y_i)
    i += 1
    x_i = x_i + step

plt.plot(x_values_euler, y_values_euler, label='Euler')
plt.plot(x_values_rk, y_values_rk, label='Runge-Kutta')
plt.plot(x_values_a, y_values_a, label='Analitic')
plt.legend()
plt.grid(True)

plt.show()
