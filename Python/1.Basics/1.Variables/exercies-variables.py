# ✅ Block — Variables.

# ➡️ Task 1: Create a variable with your age and print a message:
#       - “I am [age] years old.”

age = 28
print(f"I am {age} years old.")

#💡 Explanation:
    # - We use f-string to insert the age into a sentences.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 2: Create two varibales, a = 5 and b = 10
#      - add them and print the result.
a = 5
b = 10
result = a + b

print(result)
#💡 Explanation:
    # - We store numbers in two variables and add them using +
    # - We print the result.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 3: Create a variable for your country and print:
    # - "i live in [country]"

country = "Netherlands"

print(f"I live in {country}")
#💡 Explanation:
    # - We store the country name in a variable and print it using f-string.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4: Create a local variable inside a function and print it inside the function.

def function_1():
    variable_local = "I am a local variable."
    print(variable_local)

function_1()

#💡 Explanation:
    # - We create a local variable inside a function and print it inside the function.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: create a global variable, use it inside a function and print both inside and outside the function.

variable_global = "I am a global variable."

def function_2():
    print(variable_global)

function_2()
print(variable_global)

#💡 Explanation:
    # - We create a global variable and use it inside a function and print it inside and outside the function.

name_1 = "Luis"
age_1 = 29
city_1 = "Utrecht"

print(f"My name is {name_1}, i'm {age_1} years old and i live in {city_1}.")


#💡 Explanation:
    # - We use f-string to insert the variables into a sentences.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Difficulty Level: ⭐⭐⭐⭐

# ➡️ Task 1: Create two intenger variable. Swap their values without creating a third variable.
           #💡 Explanation:
               # - Use python's multiple assignment: a, b = b, a.
               # - This is a pythonic way to swap variables.   

a = 100
b = 1000

a, b = b, a
print(a, b)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Create a varibale that store your birth year and another with the current year. Print your age.

           #💡 Explanation: Subtract birth year from current year.
birth_year = 1996
current_year = 2025

age = current_year - birth_year
print(f"My age is {age}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Create  two float variable, divide one by the other, and arround the result to 2 decimal places.

           #💡 Explanation:
                # - Use round() function to round the result to 2 decimal places.
                # - round(division, 2)

a = 10.45
b = 2.96

result = round(a / b, 2)
print(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4.a: Create a string variable with your full name. Print the number of letters in your name(without spaces).

           #💡 Explanation:
                # - Use len() function to calculate the length of the string.
                # - len(string) -  spaces.

full_name = "Luis Da Marta"
name_lenght = len(full_name) - full_name.count(" ")
print(name_lenght)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4.b: Create a string variable with your full name. Print the number of letters in your name(without spaces).


           #💡 Explanation:
                # - Use len() function to calculate the length of the string.
                # - len(string.replace(" ", "")).

full_name1 = "Luis Da Marta"
letters_count = len(full_name.replace(" ", ""))
print(letters_count)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: Store the radius of a circle in a variable and calculate the area. Use the PI constant.

           #💡 Explanation:
                # - Use math.pi for the value of PI.
                # - Area of a circle = πr².

import math

radius = 10
area = math.pi * (radius ** 2)
print(area)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5.b: Store the radius of a circle in a variable and calculate the area. Use the PI constant.

           #💡 Explanation:
PI = 3.14159

radius = 20
area = PI * (radius ** 2)

print(f"The area is: {area}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6: Ask th user for two numbers using input(), convert them into integers, and multiply them.

           #💡 Explanation:
                # - Use int() to convert the input into an integer.
                # - Multiply the two numbers.

a = int(input("Enter 1st number: "))
z = int(input("Enter 2nd number: "))

total_1 = a * z

print(f"The result is: {total_1}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task : 

           #💡 Explanation: