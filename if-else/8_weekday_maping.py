'''
a = int(input("Enter a number (1-7)= "))

if (a == 1):
    print("It is Sunday") 

elif (a == 2):
    print("It is Monday")

elif (a == 3):
    print("It is Tuesday") 

elif (a == 4):
    print("It is Wednesday")

elif (a == 5):
    print("It is Thursday")

elif (a == 6):
    print("It is Friday") 

elif (a == 7):
    print("It is Saturday") 

else:
    print("Invalid input !! Please enter a number from 1 to 7.")
'''




'''
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

a = int(input("Enter a number (1-7)= "))

if (1 <= a <= 7):
    print(f"It is {day_list[a-1]}")
else:
    print("Invalid input !! Please enter a number from 1 to 7.")
'''




day_dict = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}
a = int(input("Enter a number(1-7): "))

if(1 <= a <= 7):
    print(f"It is {day_dict[a]}")

else:
    print("Invalid input! Please enter a number from 1 to 7.")