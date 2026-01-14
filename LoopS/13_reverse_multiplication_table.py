# multiplication table in reverse order

n = int(input("Enter a number: "))

'''
for i in range(10, 0, -1):          # for i in reversed(range(1, 11)):
    print(f"{n} x {i} = {n*i}")

'''

i = 10
while(i >= 1):
    print(f"{n} x {i} = {n*i}")
    i -= 1