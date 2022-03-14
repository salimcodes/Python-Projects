#Code by Salim O. Oyinlola

import os

print("If the three by three matrix A is given in the form shown below, Input your values for the respective variables ")
print("This program will return the determinant of the three by three matrix")
print("[a,b,c]")
print("[d,e,f]")
print("[g,h,i]")
a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
c = float(input("Input the value of c: "))
d = float(input("Input the value of d: "))
e = float(input("Input the value of e: "))
f = float(input("Input the value of f: "))
g = float(input("Input the value of g: "))
h = float(input("Input the value of h: "))
i = float(input("Input the value of i: "))
determinant = ((a*e*i)-(a*f*h)-(b*d*i)+(b*f*g)+(c*d*h)-(c*e*g))
print("The Determinant of the matrix is: " + str(determinant))

os.system("PAUSE")

#Twitter @kylieyying: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes

