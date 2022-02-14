# Python caclculator project
# Functions include: Addition, Subraction, Multiplication, Division, And Unit conversion

print("Select an operation to perform")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. CONVERT")


def add():
    print(num1 + num2)
def subtract():
    print(num1 - num2)
def multiply():
    print(num1 * num2)
def divide():
    print(num1 % num2)

 # def convert():
#    if word == "cm"
#        print()
operation = input()
if operation == 1:
    num1 = input(int("Enter first number"))
    num2 = input(int("Enter Second Number"))
    print("The result is: " + add)
elif operation == 2:
    print("The result is: " + subtract)
elif operation == 3:
    print("The result is: " + multiply)
elif operation == 4:
    print("The result is: " + divide)
# code to look for the specific units in whatever text is inputted so that the program would run
# whatever code assigned to that unit
#elif operation has cm:
    # code for what the unit should be converted to
else:
    print("INVALID ENTRY")

