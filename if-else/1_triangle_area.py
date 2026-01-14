import math
a = int(input("enter side: "))
b = int(input("enter side: "))
c = int(input("enter side: "))

s = (a+b+c)/2
if(((a + b) > c) and ((b + c) > a) and ((a + c) > b)):

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)

else:
    print("wrong")