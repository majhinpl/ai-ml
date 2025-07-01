# Data cleanining

"""
split() # split in the space by defauly
capitalize() # First letter in the sentence will make capital
title() # First letter of every word will make capitalize

"""
"""
name = "   ---nephx @@ neps 1121 _ "
clean_name = name.strip(" -12_").replace(" @@ ", " ")
print(clean_name.capitalize())

# first_name nephx and last_name = neps

first_name, last_name = clean_name.split()
"""

"""print(first_name)
print(last_name)
print(clean_name.split())
"""


"""
name = "Altitude Attitude Alpha"
firstname, middle, lastname = name.split()
print(firstname)
print(middle)
print(lastname)

"""

"""
name = "Altitude. Attitude. Alpha."
firstname, middle, lastname = name.strip(".").replace(". ", " ").split(". ")
print(firstname)
print(middle)
print(lastname)
"""

"""
name = "  __-- firoj ##&& karki 123 @@"
new_name = name.strip(" _-123@").replace(" ##&& ", " ").title()

first_name, last_name = new_name.split()
print(first_name)
print(last_name)

name = "Altitude. Attitude. Alpha."
firstname, middle, lastname = name.strip(".").replace(". ", " ").split()
print(f"firstname : {firstname}")
print(f"middle : {middle}")
print(f"lastname : {lastname}")


"""

"""
# Task2 
name = "  __--&*) firoj ##&& karki 123 @@("

result
first_name = firoj
last_name = Karki



name = "  __--&*) firoj ##&& karki 123 @@("

print(name)
clean_name = name.strip(" _-&*)123@(").replace(" ##&& ", " ").title()
first_name, last_name = clean_name.split()
print(f"first_name : {first_name}") 
print(f"last_name : {last_name}") 

"""

task = " $$ Samip ** % (+977)9842123546 "
# first_name = Samip
# ph_no = 9842123546

clean_task = task.strip(" $").replace(" ** % (+977)", " ").capitalize()
first_name, ph_no = clean_task.split()
print(f"first_name : {first_name}")
print(f"ph_no : {ph_no}")

