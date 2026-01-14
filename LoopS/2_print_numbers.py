# descending order

a = int(input("Enter starting: "))
b = int(input("Enter ending:"))

if(a < b):
    print("Invalid ! starting should be greater than ending number")

else:
    for i in range(a, b-1, -1):
        print(i, end=", ")

    '''
    while(a >= b):
        print(a, end=", ")
        a -= 1
    '''