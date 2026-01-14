#Fahrenheit to Celsius and vice-versa

print("=> Fahrenheit to Celsius.....1")
print("=> Celsius to Fahrenheit.....2")
choice = int(input("Choose 1 or 2: "))

if(choice == 1):
    far = float(input("Enter temperature in Fahrenheit: "))
    cel = 5*((far-32)/9)
    print(f"Temperature in Celsius is = {cel:.2f}")

elif(choice == 2):
    cel = float(input("Enter temperature in Celsius: "))
    far = (9*(cel/5)) + 32
    print(f"Temperarture in Fahrenheit is = {far:.2f}")

else:
    print("Invalid input!")