x = input("choose your Group (A or B): ")
y = int(input("choose your cycle (1 to 13): "))

if(x == 'A'):
    if(y == 1 or y == 3 or y == 5 or y == 7 or y == 9 or y == 11 or y == 13):
        print("\nSunday : ME(drawing)")
        print("Monday : ")
        print("Tuesday : ")
        print("Wednesday : analog")
        print("Thursday : DELC(digital)")
    elif(y == 2 or y == 4 or y == 6 or y == 8 or y == 10 or y == 12):
        print("\nSunday : DELC(digital)")
        print("Monday : ")
        print("Tuesday : ")
        print("Wednesday : signal")
        print("Thursday : cse")

elif(x == 'B'):
    if(y == 1 or y == 3 or y == 5 or y == 7 or y == 9 or y == 11 or y == 13):
        print("\nSunday : DELC(digital)")
        print("Monday : ")
        print("Tuesday : ")
        print("Wednesday : signal")
        print("Thursday : cse")
    elif(y == 2 or y == 4 or y == 6 or y == 8 or y == 10 or y == 12):
        print("\nSunday : ME(drawing)")
        print("Monday : ")
        print("Tuesday : ")
        print("Wednesday : analog")
        print("Thursday : DELC(digital)")