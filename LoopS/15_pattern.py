'''print the pattern:
1   
1 2   
1 2 3   
1 2 3 4   
1 2 3 4 5   
......... 
1 2 3 4 5 6 7 8 ...... n 
'''


'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(column, end=" ")
    print("\n", end="")         # or just use print() only, it works same
'''

n = int(input("Enter a number: "))

row = 1
while(row <= n):
    column = 1
    while(column <= row):
        print(column, end=" ")
        column += 1
    print("\n", end="")         # or just use print() only, it works same
    row += 1