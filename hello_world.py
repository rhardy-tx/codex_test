# This program is a simple calculator.
# It asks the user to choose an operation: add, subtract, multiply, or divide.
# Then it asks for two numbers and prints the result.
# added a new commetn line
# comment 1. Calculator overview

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero."
    return first_number / second_number


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an option: ")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if choice == "1":
    print(add(first_number, second_number))
elif choice == "2":
    print(subtract(first_number, second_number))
elif choice == "3":
    print(multiply(first_number, second_number))
elif choice == "4":
    print(divide(first_number, second_number))
else:
    print("Invalid choice.")
