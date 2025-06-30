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

'''
split()
capatalize()
title()
'''
name = "   ---sujata @@ pathak 1 2 3 __  "
#sujata @@ pathak
new_name = name.strip(" -123_")
print(new_name)

new_name1 = new_name.replace(" @@ ", " ")
print(new_name1)
# sujata pathak = Sujata Pathak
new_name_final = new_name1.title()
print(new_name_final)

# first_name = Sujata and last_name = Pathak
'''
after breaking 
first part -> first name 
last part -> last name
'''

first_name, last_name = new_name_final.split()
print(first_name)
print(last_name)

myname = "nephx"
print(myname.upper())

name = "  __-- firoj ##&& karki 123 @@"

"""
first_name = Firoj
last_name - Karki

"""

name.strip(" _-123@ ").replace(" ##&& ", " ")
print(new_name)