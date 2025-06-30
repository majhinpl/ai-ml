# checking the type of veriables.
number = 1
name = "nephx"
point = 1.4
is_true = False

"""print(type(number))
print(type(name))
print(type(point))
print(type(is_true))"""

# input string

"""
int()
float()
bool()
str()

"""
"""
your_name = input("input your name : ")
number = int(input("int input : "))
bollean = bool(input("bol input : "))

print(your_name)
print(number)
print(bollean)

"""
"""
# seperation
print("This is the day one of AI/ML class")
print("This", "is", "the", "day", "one", "of", "AI/ML", "class", sep = " @ ")

"""

# end = # default parameter is \n
"""
print("Hello world")
print("Hello", "world")

print("Hello", end = " # " )
print("world" )

"""


# "This" @ "is" @ "the" # "day" # "one" @ "of" @ "AI/ML" # "class"

"""
print("This", "is", "the", "day", sep = " @ ", end=" # ")

print("one", "of", "AI/ML", "class", end=" # ")

"""

# F string

num = 1

print("the number is : ", num)

print(f"the number is {num} ")

name = "nephx"
print(f"my name is : {name}")

float = 1.2
print(f"my name is : {float}")

print(f"to fixed the floating number: {float: .3f}")
