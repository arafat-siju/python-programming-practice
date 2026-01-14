'''Write a program that can reverse an integer number. example:
input: 26, output: 62 
input: 856, output: 658 
input: 14730, output: 03741 '''

n = int(input("enter an integer: "))

reversed_num = 0
while(n != 0):
    remainder = n % 10
    reversed_num = (reversed_num*10) + remainder

    n = n/10        # recommendation: just use (n = n // 10) instead of line 13 and 14
    n= int(n)       # / does floating-point division and // is integer division

print(f"reversed number = {reversed_num}")