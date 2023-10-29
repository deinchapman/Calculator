def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Cannot calculate modulus with zero."

def exponentiation(x, y):
    return x ** y

def floordivide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error: Cannot floor divide by zero."

while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentialize")
    print("7. Floor divide")

    # take input from the user
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == '6':
            print(f"{num1} ** {num2} = {exponentiation(num1, num2)}")

        elif choice == '7':
            print(f"{num1} // {num2} = {floordivide(num1, num2)}")

        # check if user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != "yes":
            break
    else:
        print("Invalid Input")
