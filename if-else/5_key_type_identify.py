# program that can say whether it is Character, digit or functional key

ch = input("Enter a key: ") 

if('A' <= ch <= 'Z'):       # ch >= 'A' and ch <= 'Z'
    print("It is an Upperchase character")

elif('a' <= ch <= 'z'):     # ch >= 'a' and ch <= 'z'
    print("It is a lowercase character")

elif('0' <= ch <= '9'):     # ch >= '0' and ch <= '9'
    print("It is a digit.")

else:
    print("It is a functional(speial) key.")