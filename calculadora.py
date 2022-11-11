print("\n--------------------------PYTHON CALCULATOR--------------------------")

print("\nWich calculation do you need to do?")

print("\nType the number of operation")

print('\n 1 - Sum')
print('\n 2 - Subtraction')
print('\n 3 - Multiply')
print('\n 4 - Divide')

operation = int(input("\n Type here your option: "))

num1 = float(input("\n First number: "))
num2 = float(input("\n Second number: "))

def sumOperation(num1, num2):
     print("\n Your result is: ", num1 + num2)

def subtractOperation(num1, num2):
    print("\n Your result is: ", num1 - num2)

def multiplyOperation(num1, num2):
    print("\n Your result is: ", num1 * num2)

def divideOperation(num1, num2):
    print("\n Your result is: ", num1 / num2)


if operation == 1:
    sumOperation(num1, num2)
elif operation == 2:
    subtractOperation(num1, num2)
elif operation == 3:
    multiplyOperation(num1, num2)
else:
    divideOperation(num1, num2)
    