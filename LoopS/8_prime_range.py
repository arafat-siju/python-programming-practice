# find all the prime numbers in a range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_list = []
non_prime_list = []

if start > end:
    print("Invalid input!")

else:
    for i in range(start, end+1, 1):
        if (i <= 1):
            non_prime_list.append(i)
            continue

        prime = True
        for j in range(2, int(i**0.5)+1, 1):
            if (i % j == 0):
                prime = False
                break

        if (prime == True):
            prime_list.append(i)
        else:
            non_prime_list.append(i)

    print("\nPrime numbers are:")
    print(prime_list)

    print("\nNon-prime numbers are:")
    print(non_prime_list)
