'''
1
1 2 
1 2 3
1 2
1
'''

'''
n = int(input("Enter a numner: "))
for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print("+", end=" ")
    print()

for i in range(n, 1, -1):
    for j in range(i, 1, -1):
        print("+", end=" ")
    print()
'''
# ======================================================
'''print the pattern:
    1   
   1 2   
  1 2 3   
 1 2 3 4   
1 2 3 4 5
'''

'''
n = int(input("Enter a number: "))
for i in range(1, n+1, 1):

    for j in range(1, n-i+1, 1):
        print(" ", end="")

    for k in range(1, i+1, 1):
        print(f"{k} ", end="")
    
    print()
'''    
# ======================================================
''' # odd
    *
   ***
  *****
 *******
*********
'''

'''
n = int(input("Enter a number: "))
for i in range(1, n+1, 1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")
'''
# ======================================================
'''print the pattern:
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

'''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):

    for j in range(n-i, 0, -1):
        print(" ", end="")

    for k in range(1, i+1, 1):
        print(f"{k} ", end="")
    
    print()
'''  
# ======================================================
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

'''
n = int(input("Enter a number: "))
for i in range(1, n+1, 1):

    for j in range(1, n-i+1, 1):
        print(" ", end="")

    for k in range(1, i+1, 1):
        print("*", end=" ")
    
    print()

for i in range(n-1, 0, -1):

    for j in range(n-i, 0, -1):
        print(" ", end="")

    for k in range(1, i+1, 1):
        print("*", end=" ")
    
    print()
'''