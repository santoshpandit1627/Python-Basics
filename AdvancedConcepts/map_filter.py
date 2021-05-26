"Normal Map"
def product10(a):
    return a * 10
r1 = range(10)
##map(product10, r1)
print (list(map(product10, r1)))

"Using Lamda"
print(list(map((lambda a: a * 10),r1)))

"Filter : like conditional statement"
print (filter((lambda a: a > 5),r1))