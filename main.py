import numpy as np
import matplotlib.pyplot as plt
from function import density_from_height
import input_data

time_array = []
height_array = []

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

def density_from_height(h): 
    return(1.225 * np.exp(1)**(-h/input_data.scale_height))

def velocity_from_height(h):
    return((input_data.gravity_const_earth / (input_data.radius_earth + h))**(0.5))


height_i = input_data.start_orbite_height
const_data = -(((input_data.start_orbite_height**2)*input_data.coeff_drag_sat*input_data.area_sat)/(input_data.mass_sat*(input_data.gravity_const_earth)**0.5)) #independemence chapter equation


time_i = 0
while(height_i>input_data.end_orbit_height):
    height_i = height_i + input_data.step*(density_from_height(height_i)*(velocity_from_height(height_i)**3))*const_data
    time_i = time_i + input_data.step
    time_array.append(time_i)
    height_array.append(height_i)
    print(height_i, time_i)


plt.plot(time_array, height_array)
plt.grid()
plt.show()





