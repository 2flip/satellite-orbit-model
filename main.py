import numpy
import matplotlib as plt
from function import density_from_height

#<----------------------START USER'S PARAMETRS---------------------->

#Parametrs_satellite
mass_sat = 500                          #kg
coeff_drag_sat = 2.2 
area_sat = 2                            #m^2

#Parametrs_use_satellite
time_use = 5.5                          #years

#Parametrs_orbite\enviroment
sun_active = True                       #not use yet
start_orbite_height = 550               #km, only circle orbite

#<----------------------END USER'S PARAMETRS---------------------->

#Constants
radius_earth = 6.371e6                  #m
gravity_const_earth = 3.986e14          #m^3/s^2 (G*M)
scale_height = 8                        #needles for calc density form height


#Calc_needless_parametrs
velocity_sat = (gravity_const_earth / (radius_earth + start_orbite_height))**(0.5)
force_drag = 0.5*coeff_drag_sat*area_sat*(velocity_sat**2)*density_from_height(start_orbite_height, scale_height) #parametrs not working in dt(dh)
ballisitc_coeff = mass_sat/(coeff_drag_sat*area_sat)




