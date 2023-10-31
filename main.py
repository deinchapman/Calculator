import decimal
from decimal import Decimal

# This function adds two numbers
def add(x, y):
   return x + y 

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function modulus two numbers
def modulus(x, y):
    return x % y

# This function exponentialize two numbers
def exponentation(x, y):
    return(x ** y)

# This function floor divide two numbers
def floordivide(x, y):
    return(x // y)

def float_calculator():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Exponentialize")
    print("7.Floor divide")
    print("q.back to start")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4/5/6/7/q): ")

    # check if choice is one of the four options
        if choice == "q":
                print()
                main()
        
        elif choice in ('1', '2', '3', '4','5','6','7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1': 
                    round(print(num1, "+", num2, "=", (add(num1, num2))), 2)

            elif choice == '2':
                round(print(num1, "-", num2, "=", subtract(num1, num2)), 2)

            elif choice == '3':
                round(print(num1, "*", num2, "=", multiply(num1, num2)), 2)

            elif choice == '4':
                try:
                    round(print(num1, "/", num2, "=", divide(num1, num2)), 2)
                except ZeroDivisionError:
                    print("Can't divide 0")
                
            elif choice == '5':
                round(print(num1, "%", num2, "=", modulus(num1, num2)), 2)

            elif choice == '6':
                round(print(num1, "**", num2, "=", exponentation(num1, num2)), 2)

            elif choice == '7':
                round(print(num1, "//", num2, "=", floordivide(num1, num2)), 2)
        
        # check if user wants another calculation
        # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
            else:
                print("Invalid Input. Returning to start")
        else:
            print("Invalid Input")
        
def decimal_calculator():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Exponentialize")
    print("7.Floor divide")
    print("q.back to start")

    while True:
        # take input from the user
        choice = input("Enter choice(1/2/3/4/5/6/7/q): ")

    # check if choice is one of the four options
        if choice == "q":
                print()
                main()
        
        elif choice in ('1', '2', '3', '4','5','6','7'):
            try:
                num1 = Decimal(input("Enter first number: "))
                num2 = Decimal(input("Enter second number: "))
            except decimal.InvalidOperation:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1': 
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                try:
                    print(num1, "/", num2, "=", divide(num1, num2))
                except decimal.DivisionByZero:
                    print ("Can't divide 0")       
            
            elif choice == '5':
                print(num1, "%", num2, "=", modulus(num1, num2))

            elif choice == '6':
                print(num1, "**", num2, "=", exponentation(num1, num2))

            elif choice == '7':
                print(num1, "//", num2, "=", floordivide(num1, num2))
                
            
        
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
            elif next_calculation == "yes":
                print()
                continue
            else:
                print("Invalid Input. Returning to start")
        else:
            print("Invalid Input")

    
def main():
    while True:
        print("Use floats or decimals for calculations?")
        choice = input("Input: (d) for decimals/ (f) for floats: ")
        if choice == "d":
            decimal_calculator()
    
        elif choice == "f":
            float_calculator()
        
        else:
            print()
            print("Please enter invalid input")
            print()
            continue

main()
        
    
