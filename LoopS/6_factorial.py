# Find factorial

n = int(input("Enter a number: "))

i = 1
product = 1

'''
for i in range(1, n+1, 1):
    product *= i
'''
while(i <= n):
    product = product * i   # product *= i

    i += 1

print(f"factorial of {n} is = {product}")

'''easy method
import math
n = int(input("Enter a number: "))
print(f"factorial of {n} is = {math.factorial(n)}")
'''