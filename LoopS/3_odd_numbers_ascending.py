# odd number in ascending order
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))


if(a > b):
    print("invalid! Starting should be less than ending number")

else:
    '''
    for i in range(a, b+1, 1):
        if(i % 2 != 0):
            print(i, end="")
        else:
            print(",", end=" ")
    '''

    while(a <= b):
        if(a % 2 != 0):
            print(a, end="")
        else:
            print(",", end=" ")
        
        a += 1