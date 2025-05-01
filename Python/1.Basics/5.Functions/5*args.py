""" ---🔍 *args ---"""

# --- what's --- ?
 # 🔹 *args is a {function parameter} that allows you to pass {multiple values} to a function.
 # 🔹 *args allows to pass the value {without defining} the number of values.
 # 🔹 *args group all the arguments in a { (tuple) }.


##################################################################################
# -- example 1 ) Basic example of *args --
def variable_print_args(*example_1):
    print(example_1)
variable_print_args(1,2,3) # Output: (1, 2, 3)

# 📌 Explanation:
   # - the function receives multi arguments.
   # - *args, groups them into a tuple.
   # - The function prints the tuple.
##################################################################################

# -- example 2) Looping Through *args --
def var_print_names(*names):
    for name in names:
        print(name)
var_print_names("luis", "Benthe") # Output: luis, Benthe
# 📌 Explanation:
   # - Since *args is a (tuple), we can iterate over it.
   # - The function tales multiple names as arguments.
   # - The {for loop} iterates over the tuple and prints each name.
##################################################################################

# -- example 3 ) *args for Math Operations --
def sum_number(*suma):
    return sum(suma)

print(sum_number(1,2,3,4)) # output: 10
# 📌 Explanation:
    # - Since *args collects, multiple numbers, we can perform math operations.
    # - *args collects the numbers in tuple.
    # - Sum(suma) adds them up.
    # - The function returns the total.
##################################################################################

# -- example 4) *args with other parameters --
def greet_to_users(greetings,*user):
    for user_name in user:
        print(f"{greetings}, {user_name}.")
greet_to_users("Hello", "Da marta", "user")

# 📌 Explanation:
    # - You can mix {*args} with normal parameters.
    # - The first parameter greetins is a normal string.
    # - *names collects all extra arguments into at tuple.
    # - The loop prints a greeting for each name.
##################################################################################

# -- example 5) Using *args with a default parameter --
def order_pizza(size = "Medium", *toppings):
    print(f"Ordering a {size} pizza with toppings: {toppings}")

order_pizza("small", "Double Cheese", "Pepperoni", "Olives", "honey")
 # output : Ordering a small pizza with toppings: ('Double Cheese', 'Pepperoni', 'Olives', 'honey')

# 📌 Explanation:
    # - You can set default values while using *args.
    # - The first argument (size) is a normal parameter.
    # - *toppings collects all  {arguments}, in this case, extra toppings in a tuple.
    # - The function prints the pizza order.
##################################################################################

# -- example 6) Using *args with Lists.
def list_numbers(*numbers):
    print(numbers)
numbers = [1,2,3,5,0]
list_numbers(*numbers) # output: (1, 2, 3, 5, 0)

# 📌 Explanation:
    # - You can unpack a list into *args.
    # - The * unpacks the list into separate values.
##################################################################################

# -- example 7) 
def inf_person(name, age, *hobbies):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
inf_person("Luis", 29, "coding", "mindset", "entrepreneurship")
# 📌 Explanation:
    # - You can use both {normal parameters} and {named parameters}.
    # - Name and Age are normal parameters.
    # - {*hobbies} collects all extra values in a tuple.
    # - The function prints the name, age, and hobbies.
##################################################################################
