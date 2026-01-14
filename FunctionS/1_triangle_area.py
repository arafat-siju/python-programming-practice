import math

def triangle_sides():
    try:
        x = float(input("Enter side: "))
        y = float(input("Enter side: "))
        z = float(input("Enter side: "))
        return x, y, z
    except ValueError:
        print("Invalid input! Please enter numeric values.\n")
        return triangle_sides()

def area(p, q, r):
    s = (p + q + r) / 2
    area = math.sqrt(s * (s - p) * (s - q) * (s - r))
    return area


a, b, c = triangle_sides()

if ((a + b > c) and (b + c > a) and (a + c > b)):
    print(f"{area(a, b, c):.2f}")
else:
    print("invalid Triangle!")