def dec_to_binary(x):
    if(x > 1):                                       
        dec_to_binary(x // 2)           
    print(x % 2, end="")           

try:
    n = int(input("Enter a Decimal number: "))
    if(n < 0):
        print("Enter positive integer please.")
    else:
        print("Binary is: ", end="")
        dec_to_binary(n)

except ValueError:
    print("Enter integer.")