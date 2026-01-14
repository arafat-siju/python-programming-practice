# find the number of and sum of all integers greater than 50 and less than
#   300 that are divisible by 9.

count = 0
sum = 0
'''
for i in range(51, 300, 1):
    if(i % 9 == 0):
        print(i, end = ", ")
        sum += i
        count += 1
'''

i = 51
while(i < 300):
    if(i % 9 == 0):
        sum += i
        count += 1
    i += 1

print(f"\n\nnumber of integers= {count}")
print(f"\nSum om integers= {sum}")
