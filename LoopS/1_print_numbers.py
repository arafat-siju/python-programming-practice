# ascending order
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if(start > end):
    print("invalid! Starting should be less than ending number")

else:
    '''
    for i in range(start, end+1, 1):
        print(i, end = "  ")

    '''

    while(start <= end):
        print(start, end = "  ")
        start += 1


