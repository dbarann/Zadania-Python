from math import sqrt

a = 2
b = 5
c = 1
delta = (b*b - 4*a*c)
x1 = (-b - sqrt(delta))/(2*a)
x2 = (-b + sqrt(delta))/(2*a)
print ("x1 = " + str(x1))
print ("x2 = " + str(x2))