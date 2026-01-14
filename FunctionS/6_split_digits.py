def separate_digits(n):
    digits = []
    while (n > 0):
        digits.append(n % 10)  
        n //= 10     
    return digits[::-1]         # reverse the list
    #return list(reversed(digits))

try:
    n = int(input("Enter an integer: "))
    if (n < 0):
        print("Please enter a positive integer.")
    else:
        digits = separate_digits(n)
        print("Digits separated:", digits)
except ValueError:
    print("Invalid input!")