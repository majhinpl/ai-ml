# Error
# print("Hello World) # Syntax Error

# Exceptions -> runtime errors 

"""

try: 
    x = int(input("Enter a number : "))

except ValueError:
    print("please enter an integer")

else:
    print(f"number = {x}")


while True:
    try : 
        x = int(input("Enter a number : "))
    except ValueError:
        print("Please Enter an integer!!")
    else :
        break

print(f"The input number in : {x}")


"""

# Division by zero error
# task -> WAP takes a number -> devide 10 by the enter number.
"""
while True:
    try:
        x = int(input("Enter a number : "))
        result = 10 / x
    except ValueError:
        print(ValueError)
    except ZeroDivisionError:
        print(ZeroDivisionError)
    else:
        print(f"Result = {result}")
        break 


num = int(input("Enter a number"))

    
"""

# WAP -> take 3 numbers as input sum, product and operation =  (num1 + num2 )/ num3
while True:
    try: 
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter a number : "))
        num3 = int(input("Enter a number : "))

        operation = (num1 + num2 )/ num3
    except (ValueError, ZeroDivisionError):
        pass
    else:
        sum = num1 + num2 + num3
        product = num1 * num2 * num3
        print(f"Sum : {sum}")
        print(f"Product : {product}")
        print(f"Sum : {operation}")
    break