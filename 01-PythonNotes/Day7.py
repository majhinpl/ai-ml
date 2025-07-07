# Functions
# user defined functions
# Task a program that greets the user


"""
def greet_user(user_name = "neps"):
    print("Welcome ", user_name)

def main():
    name = input("Enter your name ") 
    greet_user()   
    greet_user(name)

main()


# task2 -> temperature convertor celsius to fahrenheit. 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit

def main():
    celsius = float(input("Enter the temperature in celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Tempareture in farenheit : {fahrenheit: .2f} degree fahrenheit")

main()


# Task 3 : Write a program to find the maxium among 3 numbers.
def max_three_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    greatest = max_three_num(num1, num2, num3)
    print(f"The greatest number among {num1}, {num2}, {num3} = {greatest}")

main()


def max_three_num(num1, num2, num3):
    return min(num1, num2, num3)

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    smallest = max_three_num(num1, num2, num3)
    print(f"The greatest number among {num1}, {num2}, {num3} = {smallest}")

main()

"""

# Task 4: Build a simple calculator that performs addition,  subtraction, multif, and division of 3 numbers according to the user input using concept of function programming

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    print("Your Calculator")

    data = input("Your inputs : ")

    print(data)


main()