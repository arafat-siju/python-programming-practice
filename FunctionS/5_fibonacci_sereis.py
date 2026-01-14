def fibonacci(n):
    a = 0
    b = 1
    while(a <= n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

try:
    n = int(input("Enter number: "))
    if(n >= 0):
        print("Fibonacci series is: ")
        fibonacci(n)
except ValueError:
    print("invalid input!")