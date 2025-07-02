# Data structure.

"""
lists
sets
tuples
dictionaries

"""

"""
# List
mutable data structure.

# tuples
imutable

# set
strole a unique value and unorder

# dictionaries
it has key and value pair 
key should be unique and imutable.

"""

# lists = [1,2,3, "nephx", True, 9.2]
# empty list = []

"""

list = [0, 2, "nephx", False, 4.2]
print(list)
print(type(list))

# indexing
list2 = ["nephx", "ram", 32, True, False]
print(list2[0])

"""

"""
if we have n elements in a list:
the we range of index will be (n - 1)

for example if we have 10 elements:
range: 0 to 9

"""

"""
# -1 index gives the last element
list2 = ["nephx", "ram", 32, True, False]
print(list2[-2])


x = [1,2,3,4,5,6,7,8,9]
sq_x = [a ** 2 for a in x ]
print(x)
print(sq_x)

x = [3.2, 4.1, "Ramu", "Shyam", "Red Bull", 3.5, "Gita", "TensorFlow", "NumPy"]

# slicing list[starting_index : ending index] index 1 to 7

print(x[1:6])
print(x[1:])
print(x[:8])
print(x[-4:])
print(x[::-1])



# Function for the list
x = [3.2, 4.1, "Ramu", "Shyam", "Red Bull", 3.5, "Gita", "TensorFlow", "NumPy"]

x.append("Added")
print(x)

# insert(1, "hari") -> (index, value)
x.insert(0, "hari")
print(x)

# sorting

my_list = [33,65,78,99,10,43,11,0,1,3]

my_list.sort(reverse=True)
my_list.reverse()

print(my_list)


# pop - delete the last element and return the value.

x = [3.2, 4.1, "Ramu", "Shyam", "Red Bull", 3.5, "Gita", "TensorFlow", "NumPy"]

print(x.pop())
print(x)

# append = add in last(not return)  pop=remove last(return)

# remove - first of two value will delete
# clear - clear all the lists value.
x.insert(4, "Ramu")
x.remove("Ramu")

"""

"""
Tuples -> imutable, indexing and slicing same as list


my_tuples = (3,4,5,6,7,"ram", 4.5, True, 5, 5, 5, 1,1,1,1,1)

print(my_tuples)
print(type(my_tuples))

# index 
print(my_tuples.index(1))

my_tuples = (1,) # to make single tuples needs
print(type(my_tuples))


# Set - stores a uniq values and is unordered

my_set = {1, 2, 3, 4, 2 , 3}
print(my_set)
print(type(my_set))

my_set.add(5)
print(my_set)

my_set.remove(1)
print(my_set)

my_set = set() # declare empty set

"""

# dictionary  - key value pair. the key must be unique and imutable.

my_dict = {
    "name" : "nephx",
    "age" : 23,
    "ph_no" : 99999999990
}

print(my_dict)
print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())

# the remainng function of dict and how to delete a particular function

print(my_dict.get("name"))

print(my_dict.items())

my_dict.update({"update": "name"})
print(my_dict)

del my_dict["update"]
print(my_dict)
