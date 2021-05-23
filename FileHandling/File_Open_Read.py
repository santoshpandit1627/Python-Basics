# Reading and Opening Files
myfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/routers.txt", "r")
print(myfile.mode)
print(myfile.read())
print(myfile.tell())
print(myfile.read(5))
print(myfile.seek(0))
print(myfile.read(5))
print(myfile.tell())
print (myfile.readline())
print (myfile.readline())

print (myfile.seek(0))
print (myfile.readlines())

#reading network components starting from S

myfile.seek(0) # taking the curser to the beginning
for line in myfile.readlines():
    if line.startswith('s') | line.startswith('S'):
        print (line)


