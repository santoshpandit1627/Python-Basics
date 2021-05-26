"Interators and Generators"
"Normal Internation without using Internation functions"

my_list = [1, 2, 3, 4, 5, 6, 7]
for elements in my_list:
    print (elements)
"Interators"
my_iter = iter(my_list)
type(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


"Generators"
def my_gen(x, y):
    for i in range(x):
        print ("i is %d" %i)
        print ("i is %d" %y)
        yield i * y

my_object = my_gen(10,5)
print(next(my_object))


"Generator expression"
gen_exp = (x for x in range(5))
print(next(gen_exp))
