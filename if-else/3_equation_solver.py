# Quadratic Equation Solver

import math
a = float(input("enter coefficient of x2 = "))
b = float(input("enter coefficient of x ="))
c = float(input("enter constant = "))

determinant = pow(b,2) - 4*a*c    # pow(b, 2) = b**2

if (a == 0):
    if(b == 0):
        print("no solution!")
    else:
        print(f"answer, x = {-c/b}")

elif(determinant > 0):
    print("\nTwo roots....")
    print(f"x1 = {(-b + math.sqrt(determinant))/(2*a)}")
    print(f"x2 = {(-b - math.sqrt(determinant))/(2*a)}")

elif(determinant < 0):
    print("no real roots")

elif(determinant == 0):
    print("\none solution:")
    print(f"answer is, x = {-b/(2*a)}")
