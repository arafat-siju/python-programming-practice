# Leap year calculation


try:
    yr = int(input("Enter a year: "))
    
    if ((yr % 400 == 0) or ((yr % 4 == 0) and (yr % 100 != 0))):
        print(f"{yr} is a Leap year.\n")

    else:
        print(f"{yr} is not a Leap year.\n")

except ValueError:
    print("Enter valid year.")