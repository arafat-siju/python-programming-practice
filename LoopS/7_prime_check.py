# prime or non-prime

n = int(input("Enter a number: "))

if (n <= 1):
    print(f"{n} is not a prime number.")
    exit()

else:
    prime = True
    for i in range(2, int(n**0.5) + 1, 1):       # n**0.5 = pow(n, 0.5) = math.sqrt(n)
        if (n % i == 0):
            prime = False
            break

    if (prime == True):
        print("Hurrah!")
        print(f"{n} is a prime number.")
    else:
        print("Oh nooooo!!")
        print(f"{n} is not a prime number.")
