# ------------------------ Data cleanining --------------------

"""
#Topics

lstrip()
rstrip()
strip()
replace()

"""

# name = "   My --- sister's name is sujata 1 2 3 __ " -> present data 


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
newName = name.replace(" ** ", " ")
print(newName)

name = "___Saroj Adhikari"
newName = name.lstrip("___")
print(newName)

name = "Saroj Adhikari +++++"
newName = name.rstrip(" +++++")
print(newName)

name = " --Saroj ++++ Adhikari"
newName = name.lstrip(" -").replace(" ++++ ", " ")
print(newName)

name = "  nephx  "
newName = name.strip()
print(newName)

name = "  1 nephx2  "
newName = name.strip(" 12")
print(newName)

name = "1nephx2"
newName = name.strip("21")
print(newName)

"""


# name = "    ---My --- Sister's name is Sujata 1 2 3 _ "
# name = "My Sister's name is Sujata"

# steps;

"""
1. clear the front and rear part
2. clear the middle part by using replace

"""

"""

new_name = name.strip(" -123_").replace(" --- ", " ")
print(new_name)

"""

name1 = "--- My name ___ is ram 123 karki --"
print(name1.strip("- ").replace(" 123 ", " " ).replace(" ___ ", " " ))


