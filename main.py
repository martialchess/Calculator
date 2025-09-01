from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    print("Available operations:")
    print(" ".join(operations.keys()))  # Print all symbols once
    first_value = float(input("What is the first value?: \n"))
    continue_calculation= True

    while continue_calculation:
        method = input("Pick an operation: +, -, *, /: \n")
        second_value = float(input("What is your second value?: \n"))

        calc_function = operations[method]
        result = calc_function(first_value, second_value)
        print(f"{first_value} {method} {second_value} = {result}")

        should_continue = input(f"Type 'yes' to continue with the current result: {result}, or 'no' to start fresh:\n")
        if should_continue == "yes":
            first_value = result #carry forward the result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()