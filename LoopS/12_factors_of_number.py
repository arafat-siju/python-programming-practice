'''
    Find factors of an integer number. example:
        input: 20, output: 1,2,4,5,10,20 
        input: 25,  output: 1,5,25 
        input: 30, output: 1,2,3,5,6,10,15,30
'''

n = int(input("Enter a numbr: "))

print(f"Factors of {n}:", end=" ")

'''
for i in range(1, n+1, 1):
    if (n % i == 0):
        print(i, end=", ")
'''

i = 1
while(i<=n):
    if(n % i == 0):
        print(i, end=", ")
    i += 1