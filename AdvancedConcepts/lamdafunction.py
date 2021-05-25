"Lamda Linear"
a = lambda x, y: x * y
print (a(2,3))

"Lamda Complex"
def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist
print (myfunc([100, 101, 102]))

"//"
b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
print (b([100,101,102]))