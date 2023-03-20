
L=[15,10,9,7,4,2]
L.sort()
print(L)
L.sort(reverse = True)  #descending order
print(L)
#If you want to create a new sorted list without 
# modifying the original one, you should use the sorted function instead.

L = [15, 22.4, 8, 10, 3.14]
sorted_list = sorted(L)

print(sorted_list)
sorted(L, reverse = True)   #descending
print(sorted_list)

#Sorting list of tuples

#sort by age or sort by second element
L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
L.sort(key=lambda x: x[1])
print(L)
# output
# [('Alex', 5), ('Bob', 20), ('Alice', 25)]

#Sorting a list of objects
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

L=[]
L.append(User('sajid',20))
L.append(User('jabed',25))
L.append(User('saif',22))

# Sorting in lexicographic order by 'name' field
L.sort(key=lambda x: x.name)
print([item.name for item in L])
# output: ['saif', 'jabed', 'sajid']

#Sorting in ascending order by 'age' field
L.sort(key=lambda x: x.age)
print([item.name for item in L])
# output: ['sajid', 'saif', 'jabed']

#Sorting in descending order by 'age' field
L.sort(key=lambda x: x.age,reverse=True)
print([item.name for item in L])
# output: ['jabed', 'saif', 'sajid']