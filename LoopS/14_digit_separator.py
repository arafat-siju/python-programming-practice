n = int(input("Enter a four digit integer: "))

if(1000 <= n <= 9999):
    digit_1 = n // 1000
    digit_2 = (n // 100) % 10
    digit_3 = (n // 10) % 10
    digit_4 =n % 10

    print(f"Digit seperated: {digit_1},{digit_2},{digit_3},{digit_4}")
else:
    print("Please enter a valid four-digit integer.")