import matplotlib as plt
import numpy as np
import input_data

#calculator for find density form height
def density_from_height(h): 
    return(1.225 * np.exp(1)**(-h/input_data.scale_height))

def velocity_from_height(h):
    return((input_data.gravity_const_earth / (input_data.radius_earth + h))**(0.5))

#numeric calculator via runge-kutta
def runge_kutta_height(height_massiv, time_massiv):
    height_i = input_data.start_orbite_height
    time_i = 0
    const_data = -(((input_data.start_orbite_height**2)*input_data.coeff_drag_sat*input_data.area_sat)/(input_data.mass_sat*(input_data.gravity_const_earth)**0.5)) #independemence chapter equation
    while(height_i<input_data.end_orbit_height):
        height_i = height_i + input_data.step*(density_from_height(height_i)*(velocity_from_height(height_i)**3))*const_data
        time_i = time_i + input_data.step
        height_massiv.append(height_i)
        time_massiv.append(time_i)
    return(height_massiv, time_massiv)    

            


    

    


