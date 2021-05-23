newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w")
newfile.write("I like Python!")
newfile.close()
#print (newfile.read())
newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w")
newfile.write("This is a great day for science")
newfile.close()
#Override the data in the file as we are opening it again
newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w")
newfile.writelines(["Cisco","Juniper","HP"])
newfile.close()

newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w")
newfile.writelines(("Cisco","Juniper","H1"))
newfile.close()


newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "a")
newfile.writelines("\nThe string is appended")
newfile.close()

newfile = open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w+")
newfile.writelines("\nThe string is suspended for reading")
print (newfile.read())
newfile.close()



## With for Close() - no explicit close method

with open("//Users/xspt1/PycharmProjects/FileHandling/Filehandling/newfile.txt", "w") as f:
    f.write("Hello Python!")
