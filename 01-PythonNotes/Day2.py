# Data cleanining

"""

lstrip()
rstrip()
strip()
replace()

"""
"""
name = "   nephx"
newName = name.lstrip()
print(newName)


name = "nephx    "
newName = name.rstrip()
print(newName)


name = "   nephx    "
newName = name.rstrip().lstrip()
print(newName)


name = "Saroj ** Adhikari"
newName = name.replace(" ** ", " ").lstrip()
print(newName)

name = "___Saroj Adhikari"
newName = name.lstrip("___")
print(newName)


name = "Saroj Adhikari +++++"
newName = name.rstrip(" +++++")
print(newName)


name = "Saroj ++++ Adhikari"
newName = name.replace("++++", " ")
print(newName)

name = "  nephx  "
newName = name.strip()
print(newName)

name = "1nephx2"
newName = name.strip("21")
print(newName)

"""

name = "    ---My --- Sister's name is Sujana 1 2 3 _ "

# name = "My Sister's name is Sujana"

# steps;

"""
1. clear the front and rear part
2. clear the middle part by using replace

"""