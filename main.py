import numpy as np
import matplotlib.pyplot as plt
from function import density_from_height, runge_kutta_height, euler_height
import input_data

time_array = []
height_array = []
time_array_e = []
height_array_e = []


#Calc_needless_parametrs
start_velocity_sat = (input_data.gravity_const_earth / (input_data.radius_earth + input_data.start_orbite_height))**(0.5)
start_force_drag = 0.5*input_data.coeff_drag_sat*input_data.area_sat*(start_velocity_sat**2)*density_from_height(input_data.start_orbite_height) #parametrs not working in dt(dh)
ballisitc_coeff = input_data.mass_sat/(input_data.coeff_drag_sat*input_data.area_sat)


print("Start_velocity:  ")
print(start_velocity_sat)
print("Start_force_drag:  ")
print(start_force_drag)
print("Ballistic_coefficient:  ")
print(ballisitc_coeff)



#runge_kutta_height(height_array, time_array)
euler_height(height_array_e, time_array_e)

time_array_e = np.array(time_array_e)
time_array_e = time_array_e * 3.171e-8
plt.title("Продолжительность нахождения КА на орбите без двигателей")
plt.ylabel("Высота, [км]")
plt.xlabel("Время, [лет]")
plt.ylim(100, (input_data.start_orbite_height+25))
plt.plot(time_array, height_array, label="Runge-Kutta")
plt.plot(time_array_e, height_array_e, label="Euler")
plt.legend()
plt.grid()
plt.show()





