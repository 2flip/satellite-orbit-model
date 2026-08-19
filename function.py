import matplotlib as plt
import numpy as np
import input_data

#calculator for find density form height
def density_from_height(h): 
    return(1.225 * np.exp(1)**(-h/input_data.scale_height))

def velocity_from_height(h):
    return((input_data.gravity_const_earth / (input_data.radius_earth + h))**(0.5))


#numeric calculator via euler
def euler_height(height_array, time_array):
    height_i = input_data.start_orbite_height
    const_data = -(((input_data.start_orbite_height**2)*input_data.coeff_drag_sat*input_data.area_sat)/(input_data.mass_sat*(input_data.gravity_const_earth)**0.5)) #independemence chapter equation
    time_i = 0
    while(height_i>input_data.end_orbit_height):
        delta_height = input_data.step*(density_from_height(height_i)*(velocity_from_height(height_i)**3))*const_data
        height_i = height_i + delta_height
        time_i = time_i + input_data.step
        time_array.append(time_i)
        height_array.append(height_i)
        print(delta_height, height_i, time_i)
    return(height_array, time_array)    


#numeric calculator via euler
def runge_kutta_height(height_array, time_array):
    height_i = input_data.start_orbite_height
    const_data = -(((input_data.start_orbite_height**2)*input_data.coeff_drag_sat*input_data.area_sat)/(input_data.mass_sat*(input_data.gravity_const_earth)**0.5)) #independemence chapter equation
    time_i = 0
    while(height_i>245):
        k_1 = density_from_height(height_i)*velocity_from_height(height_i)*const_data
        k_2 = density_from_height(height_i+((input_data.step*k_1)/2))*velocity_from_height(height_i+(input_data.step/2))*const_data
        k_3 = density_from_height(height_i+((input_data.step*k_2)/2))*velocity_from_height(height_i+(input_data.step/2))*const_data
        k_4 = density_from_height(height_i+(input_data.step*k_3))*velocity_from_height(height_i+(input_data.step))*const_data
        delta_height = (input_data.step/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        height_i = height_i + delta_height
        time_i = time_i + input_data.step
        time_array.append(time_i)
        height_array.append(height_i)
        print(delta_height, height_i, time_i)
    return(height_array, time_array)    



    

    


