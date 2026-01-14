# Fibonacci series up to n

n = int(input("Enter a Number: "))

a = 0
b = 1

while(a <= n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c


'''
for i in range(n):
    if(a > n):
        break
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c
'''