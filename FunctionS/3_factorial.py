# find factorial with recursion

def fact(n):
    if (n < 0):
        return None
    if (n == 0 or n == 1):
        return 1
    return n * fact(n - 1)


try:
    x = int(input("Enter a number: "))
    
    result = fact(x)
    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {x} is: {result}")

except ValueError:
    print("Invalid input! Enter an integer.")