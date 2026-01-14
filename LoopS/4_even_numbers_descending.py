# even nnumbers in descending order

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

if(a < b):
    print("Invalid ! starting should be greater than ending number")

else:
    '''
    for a in range(a, b-1, -1):
        if(a % 2 == 0):
            print(a, end="")
        else:
            print(",", end=" ")
    '''

    while(a >= b):
        if(a % 2 == 0):
            print(a, end="")
        else:
            print(",", end=" ")

        a -= 1