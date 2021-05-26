from itertools import *

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

# chain(list1, list2)
for i in chain(list1, list2):
    print (i)

#count
for i in count(10,2.5):
    if i <= 50:
        print (i)
    else:
        break

#cycle - Infinite Loop
a = range(11, 16)
for i in cycle(a):
    print (i)

#filterfalse

ifilterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])

#slice
range(10)
list(range(10))
list(range(10))[2:9:2]
"OR"
islice(range(10), 2, 9, 2)