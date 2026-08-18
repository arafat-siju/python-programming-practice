'''
fff = open("reading.txt", "r")

data = fff.read()
print(data)

fff.close()
'''

# The same can be written using with statement like this:
with open("magnet.txt", "r") as asdf:
    print(asdf.read())
# dont have to explicitly close the file, no need asdf.close()