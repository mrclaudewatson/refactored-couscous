# Name: CLaude Watson
# UID: U72087839
# Area of composite shape - To read 3 values and determine the area of a shaded region.

import math
p = float(input("Enter the length of the first side. (Do not include units):"))
q = float(input("Enter the length of the second side. (Do not include units):"))
r = float(input("Enter the length of the radius. (Do not include units):"))
kite_area = (p * q) / 2
circle_area = math.pi * r**2
area_of_shape = kite_area - circle_area
print("The shaded area is {0:,.3f} square units.".format(area_of_shape))