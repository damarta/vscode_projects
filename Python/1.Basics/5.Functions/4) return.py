# """ Return statement """

# #-----------------------------------------------------------
#     # - what's a return statement?
#         # - return is a statement that is used inside a function to return a value/store a result.
#         # - return send back the value when you need it.
#         # - return ends the function.
#         # - return is optional.

#     # - why do we need a return statement?
#         # - to return a value from a function.
#         # - to store the result of a function.
#         # - to end the function.
#         # - to return multiple values using tuples.
#         # - to return a list, dictionary, set, etc.
#         # - to return any data type.

#     # - how to use a return statement?
#         # - create a function.
#         # - use the return statement.
#         # - call the function and store the result.
#         # - print the result.

# ###########################################################################################

# # --- long way ---
# def power(x, y):
#     return x ** y
# result = power(2,4)
# print(result) # 16

# # --- short way ---
# def power(x, y):
#     return x ** y
# print(power(2,3))

# # -- Smart way --
# def power(a,b):
#     result = a / b
#     return result
# output= power(18,12)
# print(output)

# # ##-----------------------------------------------------------


# # -- Example 1 --
# def greet(name, last_name):
#     greeting = f"Hello, {name} {last_name}"
#     return greeting

# # Calling the function and storing the returned value
# greeting = greet("Luis", "Da Marta")
# print(greeting)  # Output: Hello, Luis Da Marta
# ##-----------------------------------------------------------


# # -- example 2 --
# def greet(name, last_name):
#     message = f"Hello, {name} {last_name}!"
#     return message

# # Asking the user for input
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Calling the function and storing the result
# message = greet(first_name, last_name)

# print(message)  # Output depends on user input
# ##-----------------------------------------------------------


# # -- Example 3 --
# def user_info(name, last_name):
#     full_name = f"{name} {last_name}"
#     name_length = len(full_name)
#     return full_name, name_length  # Returns a tuple

# # Get user input
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Get multiple return values
# full_name, length = user_info(first_name, last_name)

# print(f"Full Name: {full_name}")
# print(f"Name Length: {length} characters")

# -- example 4 --
def calculate(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div  # Returns a tuple

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Get multiple return values
add, sub, mul, div = calculate(num1, num2)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

# -- example 5 --
# """ Return statement """

# #-----------------------------------------------------------
#     # - what's a return statement?
#         # - return is a statement that is used inside a function to return a value/store a result.
#         # - return send back the value when you need it.
#         # - return ends the function.
#         # - return is optional.

#     # - why do we need a return statement?
#         # - to return a value from a function.
#         # - to store the result of a function.
#         # - to end the function.
#         # - to return multiple values using tuples.
#         # - to return a list, dictionary, set, etc.
#         # - to return any data type.

#     # - how to use a return statement?
#         # - create a function.
#         # - use the return statement.
#         # - call the function and store the result.
#         # - print the result.

# ###########################################################################################

# # --- long way ---
# def power(x, y):
#     return x ** y
# result = power(2,4)
# print(result) # 16

# # --- short way ---
# def power(x, y):
#     return x ** y
# print(power(2,3))

# # -- Smart way --
# def power(a,b):
#     result = a / b
#     return result
# output= power(18,12)
# print(output)

# # ##-----------------------------------------------------------


# # -- Example 1 --
# def greet(name, last_name):
#     greeting = f"Hello, {name} {last_name}"
#     return greeting

# # Calling the function and storing the returned value
# greeting = greet("Luis", "Da Marta")
# print(greeting)  # Output: Hello, Luis Da Marta
# ##-----------------------------------------------------------


# # -- example 2 --
# def greet(name, last_name):
#     message = f"Hello, {name} {last_name}!"
#     return message

# # Asking the user for input
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Calling the function and storing the result
# message = greet(first_name, last_name)

# print(message)  # Output depends on user input
# ##-----------------------------------------------------------


# # -- Example 3 --
# def user_info(name, last_name):
#     full_name = f"{name} {last_name}"
#     name_length = len(full_name)
#     return full_name, name_length  # Returns a tuple

# # Get user input
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Get multiple return values
# full_name, length = user_info(first_name, last_name)

# print(f"Full Name: {full_name}")
# print(f"Name Length: {length} characters")

# -- example 4 --
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error: Cannot divide by zero."
        return x / y
    else:
        return "Invalid operation."

while True:
    print("\nChoose an operation: add, subtract, multiply, divide")
    operation = input("Enter operation (or type 'exit' to quit): ").lower()

    if operation == "exit":
        print("Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")