# dec to bin

n = int(input("Enter a decimal number: "))

binary = ""

if n == 0:
    binary = "0"

while(n > 0):
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

print("Binary is: ", binary)



'''
def dec_to_bin(n):
    if(n > 1):
        dec_to_bin(n // 2)
    print(n % 2, end="")


a = int(input("Enter a decimal Number: "))
if(a == 0):
    print("binary: 0")
else:
    print("Binary is: ")
    dec_to_bin(a)

'''