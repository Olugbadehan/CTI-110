#Maisha Mage
#11/11/25
#P2LAB1
#The program will calculate the diameter, circumference, and area of a circle

import math


radius = float(input("What is the radius of the circle? "))
print()


diameter = 2 * radius


print(f"The diameter of the circle is {diameter:.1f}\n")

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {circumference:.2f}\n")

area = math.pi * radius**2

print(f"The area of the circle is {area:.3f}")


