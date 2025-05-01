""" 1) Exercise: Creating a Simple Function"""

# - 🔹 concept: Basic functions + calling a function.
    # 🔸 task: Writte a function that prints "Hello, world", when called.

# - 🔹 ejercies:

            #example 1)
def hello_wrold():
    print("hello, world :) !")

hello_wrold()

            #example 2)
def greeting():
    print("Hello User, how is going?")

greeting()

            #example 3)
def greet_2025(name):
    print(f"Hi {name}, welcome to 2025!")
greet_2025("Luis")


""" 2) Exercise: Creating a Simple Function"""

# - 🔹 concept: Parameters and Arguments
    # 🔸 task: Write a function that takes a name and prints a greeting.
# - 🔹 ejercies:

            #example 1)
def goodmorning(name):
    print(f"Good Morning {name}!")

goodmorning("Benthe")
goodmorning("Kai and Venus")



""" 3 ) Exercise: Functions with multiple parameters"""

# # - 🔹 concept: Functios with multiple parameters.
#     # 🔸 task: Write a function that takes two numbers and return their sum.

# - 🔹 ejercies:

            #example 1)
def multi_parameters(num1, num2):
    sum_1 = num1 + num2
    return sum_1
multi_parameters(11, 22)
print(sum)


# ❌ The problem in this exmaple is that i'm trying to print the sum outside the function, but {sum is a local varibale} inside the function.
# ❌ What’s Wrong?
    # 1) sum only exist inside  { multiple_parameters() }
    # 2) outside of the function, sum doesn't exist.
    # 3) { multi_parameters(11, 22) } runs, but its return value is lost because it's not stored in a varible

# ✅ Solution:
def multi_parameters(num3, num4):
    sum_result = num3 + num4
    return sum_result

total = multi_parameters(69, 1)
print(total)
    #📌 Summary of Fixes
        # ✅ Use a different name for a sum.(sum is a also a built-in function in Py)
        # ✅ Store the function return value in a variable before printing.
        # ✅ Print the correct variable (total instead of sum).

##############################################################
            #example 2)
def add_num(a,b):
    return a + b

result = add_num(1, 2)
print(result)
##############################################################
            #example 3)
def test():
    x = 10
    return x
value = test()
print(value)
    #📌 Summary of Fixes
        # ✅ test () returns {x}, so we store it in a value.
        # ✅ We print {value} instead of {x} because x only exist inside the function.


##############################################################
            #example 4)
x = 100
def test_1():
    x = 10
    return x

print(test())
print(x)




""" 4 ) Exercise: Functions with default parameter"""

# - 🔹 concept: Default parameters
     # 🔸 task: Write a function that greets a user with a default name if no name is given.


# - 🔹 ejercies:

            #example 1)
def greet (name = "Guest"):
    print(f"Hello, {name}")
greet()
greet("Luis")

##############################################################

            #example 2)
def greet_default(name = "user", numb = 1):
    greeting = f"Hello {name}, your user name is: {numb}."
    return greeting

greet1 =greet_default()
greet2 =greet_default(name = "Luis", numb = 2)

print(greet1)
print(greet2)
##############################################################
            #example 2.b)
def greet_default(name = "user", numb = 1):
    
    return f"Hello {name}, your user name is: {numb}."

# Function calls
greet1 =greet_default()
greet2 =greet_default(name = "Luis", numb = 2)

# Print results
print(greet1)
print(greet2)
# -- 📌 Suggested Improvements -- 
    #✅ Added docstring for clarity.
    #✅ Formatted Spacing for better readabbility.
##############################################################
            #example 2.c)
def greet_default(name="User", numb=1):
    #Returns a greeting message with a default name and user number.
    if not isinstance(numb, int):  
        return "Error: User number must be an integer."
    return f"Hello {name}, your user name is: {numb}."

print(greet_default("Luis", "wrong_value"))  
# Output: Error: User number must be an integer.
# -- 📌 Suggested Improvements -- 
    #✅ 


# """ 5 ) Exercise: Using *args and **kwargs"""

# # # - 🔹 concept: 
            # *args (multiple positional arguments)
            # **kwargs (multiple named arguments)

# #     # 🔸 task: write a function that takes multiple numbers and returns their sum using *args. Then, modify it to accept named arguments with **kwargs.

# # - 🔹 ejercies: *args

#             #example 1) using *args
def mult_num(*args):
    return sum(args)
print(mult_num(1,2,3,4))

print(mult_num(12,22,3,4))

#             #example 1) using *args
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(3,7))

# # - 🔹 ejercies: **kwargs

#             #example 1) using **kwargs
def sum_numbers_details(message = "Result:",**kwargs):
    total = sum(kwargs.value())
    print(f"{message}{total}")




# 📌 3 Exercises for *args.

""" 1 ) Exercise: Sum of multiple numbers"""
    

# 🔸 task: 
    # Write a function that takes multiple numbers using *args.
    # Return the sum of all the numbers.

# 📝 exercies 1):
def big_sum(*suma):
    return sum(suma)

print(big_sum(69, 69))

    # 🔍 Explanation:
        # - *args allows the function to take mutiple arguments.
        # - args is treated as a tuple -> (69,69)
        # - sum(args) adds all numbers together.

    # ✅ What you learn?
        # - *args collects multiple values into a tuple.
        # - sum(variable name) adds all the values.

# 💡 Alternative (Without sum()):
def sum_numers(*args_variable):
    total = 0
    for num in args_variable:
        total += num
    return total

print(sum_numers(68,1))

""" 2 ) Exercise: Multiply Numbers (*args)"""
    

# 🔸 task: 
    # Write a function that takes multiple numbers using *args.
    # Return their product

 # 📝 Solution:
def multipl_numbers(*multi):
    result = 1
    for num in multi:
        result *= num
    return result

# print(multipl_numbers(3,6))

#      ✅ What you learn?
        # - *args can be used for multiplicationm not just addition.
        # - A loop iterates through *args and multiplies each number.

#      🔍 Explanation:
        # 1) result = 1 (we start with 1, because 1 * anything = anything).
        # 2) We loop through args and multiply each value.
        # 3) The function returns the final product.


""" 3) Exercise: Find maxium numbers (*args)"""
    

# 🔸 task: 
    # Write a function that takes multiple numbers using *args.
    # Return the largest number.

    #Create a function that find the largest number using *args.

 # 📝 exercies:
def find_max(*args):
    return max(args)

print(find_max(111.2,111.3,111.4))

#      ✅ What you learn?
        # - max (args) find the biggest value in *args.

#      🔍 Explanation:
        # 1) *args collects all numbers into a tuple.
        # 2) max(args) returns the largest number.

#      💡 Alternative (Without max()):
def find_max(*args):
    largest = args[0]  # Assume first number is largest.
    for num in args:
        if num > largest:
            largest = num # update if a larger number is found.
    return largest

#📌 Exercises for **kwargs (Multiple Named Arguments)

""" 4 ) Exercise: Sum of multiple numbers"""
    
# 🔸 task: 
    # Write a function that takes user details like:
        # name
        # age
        # city
    # prints the information

    # Create a function that takes user details.

 # 📝 exercies:
def user_info(**info):
    for key, value in info.items():
        print(f"{key.capitalize()}, {value}")

user_info(name = "luis", age = 28, city = "Hilversum")
#      ✅ What you learn?
        # - ** kwargs.items() loops through dictionary
        # - You can pass any number of named argument.

#      🔍 Explanation:
        # 1) **kwargs collects multiple named arguments into a dictionary.
        # 2) kwargs.items() loops through key-value pairs.
        # 3) We print each key-value pair dynamically.

""" 5) Exercise: Store product prices"""

# 🔸 task: 
    # Write a function that takes multiple products and their prices using **kwargs and return total cost.

    #

 # 📝 exercies:
def total_price(**kwargs):
    return sum(kwargs.value()) # sum all the prices.

print(total_price(apple = 1.5, banana = 2.0, orange = 1.0))

#      ✅ What you learn?
        # - **kwargs.value() returns all price
        # - sum(kwargs.values()) calcilates total cost.

#      🔍 Explanation:
        # 1) **kwargs stores product names as keys and prices as values.
        # 2) kwargs.values() extracts prices.
        # 3) sum( kwargs.value() ) calculates total cost

#      💡 Alternative (Without max()):
def total_price(**kwargs):
    total = 0
    for price in kwargs.value():
        total += price
    return total

""" 6 ) Exercise: Custom Greetings (*args and **kwargs)"""

# 🔸 task: 
    # write a function that:
        # uses *args for greeting words.
        # uses **kwargs for uses details.
    #C

 # 📝 exercies:
def greet_user(*args,**kwargs):
    greeting = " ".join(args) #join.() --> joins greeting ("hello" + "Everyone")
    user_info = ", ".join([f'{key}: {value}' for key, value in kwargs.items()])
    return f"{greeting}! ({user_info})"
print(greet_user("Hello", "everyone", name = "King", age = 29, city = "casa"))
#      ✅ What you learn?
        # - *args is used for greeting words
        # - **kwargs is used for user details.

#      🔍 Explanation:
        # 1) *args collects multiple greetings and joins them into a single string.
        # 2) **kwargs collects user details.
        # 3) " ".join(args) creates a single greeting message.
        # 4) ", ".join([f"{key}: {value}" for key, value in kwargs.items()]) formats ser details.

#      💡 Alternative (Without max()):




# """ 3 ) Exercise: Functions with multiple parameters"""


# 🔸 task: 
    # 
    # 

    #C

 # 📝 exercies:

#      ✅ What you learn?
        # - 
#      🔍 Explanation:
        # 1) 

#      💡 Alternative (Without max()):

