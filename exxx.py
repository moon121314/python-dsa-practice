def grading(marks):
    if 0<= marks <= 100:
        if marks >= 90:
            return 'A'
        elif marks >= 80:
            return 'B'
        elif marks >= 70:
            return 'C'
        elif marks >= 60:
            return 'D'
        else:
            return 'F'
    else:
        return 'Invalid marks'


last_digit = 6
marks = float(input("Enter the marks obtained: ")) + last_digit
grade = grading(marks)
print("The grade is: ",grade)


#output

#Enter the marks obtained: 80
#The grade is:  B


# write  a program to find the kinetic energy of an object 

def kinetic_energy(mass, velocity):

    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

mass = 22.5
velocity = 10

ke = kinetic_energy(mass, velocity)
print("Kinetic energy: ", ke)

#output

#Kinetic energy:  1125.0

# write a program to find the force acting on an object running with an acceleration of 1400 cms(take mass = last digit of your id +)

def calculate_force(mass, acceleration):
    force = mass * acceleration

    return force 

last_digit = 8
mass = last_digit + 2
acceleration = 3

force = calculate_force(mass,acceleration)
print("Applied force: ", force)

#output
#Applied force:  30


# write a program to find the value of the following 

def calculate_product():
    product = 1
    start = 2
    end = 42
    step = 5
    
    for num in range(start, end + 1, step):
        product *= num
    
    return product

# Call the function
result = calculate_product()
print(f"Product of series = {result}")

#output
#Product of series = 84361761792


import numpy as np

last_digit = 6
first_digit = 2  
h = last_digit + first_digit  
g = 9.8  

time = np.sqrt(2 * h / g)
print(f" Height (h) = {h}m, Time to fall = {time:.3f} seconds")

#output
#Height (h) = 8m, Time to fall = 1.278 seconds

import math

def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

radius = 7.5
sphere_result = sphere_area(radius)
print(f"Radius = {radius}m, Surface Area of Sphere = {sphere_result:.2f} m^2")

#output
#Radius = 7.5m, Surface Area of Sphere = 706.86 m^2

def triangle_area(side):
    area = (math.sqrt(3) / 4) * (side ** 2)
    return area

side = 2
triangle_result = triangle_area(side)
print(f"Side = {side}m, Area of Equilateral Triangle = {triangle_result:.2f} m^2")

#output
#Side = 2m, Area of Equilateral Triangle = 1.73 m^2

def calculate_pulley_power(driver_force, driven_force, angular_velocity, radius=1):
    driver_torque = driver_force * radius
    driven_torque = driven_force * radius
    net_torque = driver_torque - driven_torque
    power = net_torque * angular_velocity
    return power, net_torque


driver_force = 35
driven_force = 24
angular_velocity = 22

power, net_torque = calculate_pulley_power(driver_force, driven_force, angular_velocity)

print(f"Driver Force = {driver_force}N, Driven Force = {driven_force}N, Angular Velocity = {angular_velocity} rad/s")
print(f"Net Torque = {net_torque} Nm, Power = {power} Watts")

#ouput
#Driver Force = 35N, Driven Force = 24N, Angular Velocity = 22 rad/s
#Net Torque = 11 Nm, Power = 242 Watts

