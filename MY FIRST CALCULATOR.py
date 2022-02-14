# Python Calculator project
# Functions include: Addition, Subtraction, Multiplication, Division

print("Using the below numbers, select an operation to perform")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

# print("5. CONVERT")
operation = input()

if operation == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second Number: "))
    add = num1 + num2
    result = str(add)
    print("The result is " + result)

elif operation == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second Number: "))
    subtract = num1 - num2
    result2 = str(subtract)
    print("The result is " + result2)

elif operation == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second Number: "))
    multiply = num1 * num2
    result3 = str(multiply)
    print("The result is " + result3)

elif operation == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second Number: "))
    divide = num1 / num2
    result4 = str(divide)
    print("The result is " + result4)

# code to look for the specific units in whatever text is inputted so that the program would run
# whatever code assigned to that unit
# elif operation has cm:
# code for what the unit should be converted to
else:
    print("INVALID ENTRY")

# def convert():
#    if word == "cm"
#        print()
