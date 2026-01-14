'''
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

a = int(input("Enter a number(1-12): "))

if(1 <= a <=12):
    print(f"It is {month_list[a-1]}")

else:
    print("Invalid input! Enter number form 1 to 12")
'''


month_dict = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

a = int(input("Enter a number(1-12): "))

if(1 <= a <= 12):
    print(f"It is {month_dict[a]}")
else:
    print("Invalid input! Enter number form 1 to 12")