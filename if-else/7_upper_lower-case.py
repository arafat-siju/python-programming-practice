# convert an upper case letter to lower case letter and vice versa

ch = input("Enter a letter= ")
 
if (ch >= 'A' and ch <= 'Z'):
    ch = ord(ch) + 32   # uppercase to lowercase

elif(ch >= 'a' and ch <= 'z'):
    ch = ord(ch) - 32   # lowercase to uppercase 
 
print(f"Converted = {chr(ch)}")