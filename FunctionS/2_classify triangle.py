# classify triangle

def get_sides():
    while (True):
        try:
            x = float(input("Enter side: "))
            y = float(input("Enter side: "))
            z = float(input("Enter side: "))
            return x, y, z
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")

def types_of_triangle(a, b, c):
    if(a == b == c):
        print("\nEquilateral Triangle", end=" - ")
        print("has three equal sides")
    elif((a == b and a != c) or (b == c and a != b) or (a == c and a != b)):
        print("\nIsosceles Triangle", end=" - ")
        print("has two equal sides")
    elif(a != b and  b != c and a != c ):
        print("\nScalene Triangle", end=" - ")
        print("has no equal sides")


a, b, c = get_sides()
if((a + b > c) and (b + c > a) and (a + c > b)):
    types_of_triangle(a, b, c)
else:
    print("Invalid Triangle.")