"Normal List"
list1 = []
for i in range(10):
    result = i ** 2
    list1.append(result)
print (list1)

"List comprehension Ordered Output"
list2 = [x ** 2 for x in range(10)]
print (list2)

"Conditional List Comprehension"
list3 = [x ** 2 for x in range(10) if x > 5]
print ( list3)

"Set Comprehension - Unordered Output"
set1 = {x ** 2 for x in range(10)}
print (set1)

"Dictionary Comprehension"
dict1 = {x : x * 2 for x in range(10)}
print (dict1)