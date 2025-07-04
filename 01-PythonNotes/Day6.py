# looping or iterative statements
# for loop
"""
fruits = ["apple", "banana", "kiwi"]
for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "kiwi", "mango", "watermelon"]
for fruit in fruits:
    print(fruit)


# list = range(start, stop, step)
my_list = list(range(1, 11, 2))
print(my_list)

for i in range(1, 21, 2):
    print(i, end=", ")

my_dic = {
    "1" : "Apple",
    "2" : "Banana",
    "3" : "Mango"
}

for k in my_dic:
    print(f"{k} : {my_dic[k]}")


fruits = ["Apple", "Mango", "Banana"]
count = 0
for fruit in fruits:
    count = count +1
    print(f"{count} : {fruit}")


count = 0
while count <= 10:
    print("i'm happy today")
    count += 1


# Break and continues 
# nested loop, pass # task
# Break -> when a particulars occurs break the Loop

for i in range(1,10):
    if (i == 9):
        break
    print(i)

"""
# continues -> when a particulars condition occurs skip the iteration
for i in range(1,10):
    if (i == 2):
        continue
    print(i)
