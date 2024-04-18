# C1a.py
#
# author: A. N. Other
# date: September 2016
side_j = int(input("Please enter the length of the base of the triange\n\n"))
side_k = int(input("Please enter the perpendicular height of the triange\n\n"))
print("\nThe area of your triange is ", side_j / 2 * side_k,"\n\n")
# Testing
'''
print("My assertions are:"
"\nj = 5, k = 4 output = 10"
"\nj = 7, k = 9 output = 31.5")
'''
# C1b.py
#
# author: A. N. Other
# date: September 2016
side_q = int(input("Please enter the length of the small rectangle\n\n"))
side_w = int(input("Please enter the width of the small rectangle\n\n"))
side_s = int(input("Please enter the length of the large rectangle\n\n"))
side_g = int(input("Please enter the width of the large rectangle\n\n"))
print("\nThe area of your shape is ", side_g * side_s - side_q * side_w,"\n\n")
# Testing
'''
print("My assertions are:"
"\nq = 5, w = 3, s = 8, g = 4 output = 17"
"\nq = 2, w = 1, s = 5, g = 3 output = 13")
'''
# C1c.py
#
# author: A. N. Other
# date: September 2016
side_u = int(input("Please enter the length of the rectangle\n\n"))
side_m = int(input("Please enter the width of the rectangle\n\n"))
side_n = int(input("Please enter the length of the side of the triangle\n\n"))
print("\nThe area of your shape is ",
side_u * side_m
+ side_n / 2 * side_n
,"\n\n")
# Testing
'''
print("My assertions are:"
"\nu = 5, m = 3, n = 5 output = 27.5"
"\nu = 2, m = 1, n = 5 output = 14.5")
'''
# C2a.py
#
# author: A. N. Other
# date: September 2016
side_x = int(input("Please enter the length of the rectangle\n\n"))
side_y = int(input("Please enter the width of the rectangle\n\n"))
print("\nThe area of your shape is ", side_x * side_y,"\n\n")
# Testing
'''
print("My assertions are:"
"\nx = 5, y = 3, output = 15"
"\nx = 7, y = 6, output = 42")
'''
# C2b.py
#
# author: A. N. Other
# date: September 2016
import math
side_x = int(input("Please enter the radius of the circle\n\n"))
print("\nThe area of your shape is ", side_x ** 2 * math.pi * 3/4 ,"\n\n")
# Testing
'''
print("My assertions are:"
"\nx = 5, output = 58.9"
"\nx = 7, output = 115.5")
'''
