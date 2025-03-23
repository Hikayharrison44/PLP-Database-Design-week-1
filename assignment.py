#  Basic calculator program 

def get_user_input():
    """Get two numbers and a mathematical operation from the user."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /)")
    return num1, num2, operation 

def perform_operation(num1, num2, operation):
    """"Perform the mathematical operation based on the user's input."""
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 !=0:
            result = num1 / num2 
        else:
            raise ValueError("Cannot divide by zero!")
    else: 
        raise ValueError("Invalid operation. Please enter +, -, *, or /.")
        return result
def main():
    num1, num2, operation = get_user_input()
    try:
        result = perform_operation(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}") 
    except ValueError as e:
        print(str(e))   

        if __name__ == "__main__": main()
