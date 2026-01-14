'''print the pattern:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(row, end=" ")
    print("\n", end="") 
'''

'''
n = int(input("Enter a number: "))

for i in range(1, n+1, 1):
    print(f"{i} " * i, end="")
    print()
'''
# ========================================================================
'''print the pattern:
A 
A B 
A B C 
A B C D 
A B C D E
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(chr(column + 64), end=" ")
    print() 
'''
# ========================================================================
'''print the pattern:
A 
B B 
C C C 
D D D D 
E E E E E
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(chr(row + 64), end=" ")
    print()  
'''
# =======================================================================
'''print the pattern:
1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(column % 2, end=" ")
    print()  
'''
# =======================================================================
'''print the pattern:
1 
0 0 
1 1 1 
0 0 0 0 
1 1 1 1 1 
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print(row % 2, end=" ")
    print()  
'''
# ========================================================================
'''print the pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'''

'''
n = int(input("Enter a number: "))

for row in range(1, n+1, 1):
    for column in range(1, row+1, 1):
        print("*", end=" ")
    print()
'''   
# ========================================================================