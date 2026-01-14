# character to ASCII and vice-versa

print("1. Character to ASCII.")
print("2. ASCII to Character.")

try:
    choice = int(input("Enter choice (1 or 2): "))

    if (choice == 1):
        ch = input("Enter a single character: ")
        if (len(ch) == 1):
            print(f"You pressed '{ch}' and its ASCII value is = {ord(ch)}")
        else:
            print("Please enter only ONE character.")

    elif (choice == 2):
        ascii_value = int(input("Enter ASCII value (0–127): "))
        if (0 <= ascii_value <= 127):
            print(f"You entered '{ascii_value}' and it is = '{chr(ascii_value)}'")
        else:
            print("Invalid ASCII value. Must be between 0 and 127.")

    else:
        print("Choose correctly (1 or 2).")

except ValueError:
    print("Invalid input. Please enter numbers only.")