# prime or non-prime number check

def prime_check(n, count):
    if(n < 0):
        print("Please enter positive number.")
        exit()
    if(n == 0 or n ==1):           
        # count = -1
        return
    for i in range(1, n+1, 1):
        if(n % i == 0):
            count += 1
    return count  

try:
    n = int(input("Enter a number: "))
    count = 0
    count = prime_check(n, count)
    if(count == 2):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is non-prime number")
except ValueError:
    print("invalid input!")