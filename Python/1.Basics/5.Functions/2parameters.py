# """--- 🔍 parameters.---"""
# # {parameters}: 
#     # - what's? 
#         # 🔹 Are the imput values that a function receives.

#     # - Why? 
#         # 🔹 Are the values that a function needs to execute.

#     # - How? 
#         # 🔹 are the values that a function receives when it is called.

# # {arguments}: 
#     # what's? 
#         # 🔹 Are the values that a function receives when it is called.

# ############################################################################

# # [ how to past parameters and argumnets to a function? ]
#     # example 1:
# def function_name(name):
#     print(f"Hi, {name}!")

# function_name("Luis")
# #-----------------------------------------------------------

# # [ how to past multiple parameters and argumnets to a function? + return ]

#     # example 1:
# def function_name(name, age):
#     print(f"Hi, {name}! You are {age} years old.")
#     return name # explain return
# function_name("Luis", 29)

# #-----------------------------------------------------------

#     # example 2:
# def my_dogs(name, age):
#     print(f"The name of my dogs is {name} and they are {age} years old.")

# my_dogs("Kai and venus", 4)
while True:
    print("\nChoose an operation: add, subtract,multiply, divide")

    operation_var = input("Enter operation (or type 'exit' to quit): ").lower()

    if operation_var == "exit":
        print("Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")