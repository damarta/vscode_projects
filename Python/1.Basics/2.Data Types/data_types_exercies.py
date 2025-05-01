# ✅ Block — Data Types.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1: Create an intenger, float, string variable, and print all three values.

           #💡 Explanation:
                # - In this task, you have to create three variables of different data types.
                # - You have to create a variable of intenger, float, and string data types.
                # - You have to print all three variables.
                # - You have to use f-string to print the variables.
                # - you use (\ n) to print the next line.

int_example = 111
float_example = 69.9
string_example = "Pinguin"

print(f"\n -This is a exampple of intenger: {int_example}.\n -This is a exmaple of float: {float_example}.\n -This is a exmaple of string: {string_example}.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Create two strings varibales, concatenate them with a space in between, and print the result.

           #💡 Explanation:

first_nam = "Luis"
last_nam = "Da Marta"

full_nam = first_nam + " " + last_nam
print(f"My full name is: {full_nam}.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Create a float variable, convert it to an integer, and print both.

           #💡 Explanation:
                # - In this task, you have to create a float variable.
                # - You have to convert the float variable to an integer.
                # - You have to print both the float and integer variables.
                # - You have to use f-string to print the variables.
                # - you use (\ n) to print the next line.

height = 1.89
height_int = int(height)

print(f"\n -This is a float height: {height}.\n -This is a intenger height: {height_int}.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4.a: Create a list with 6 elements (numbers). Print the first and last elements.

           #💡 Explanation:
            # - In this task, you have to create a list of numbers.
            # - You have to print the first and last elements of the list.
            # - You have to use f-string to print the elements.
            # - you use (\ n) to print the next line.


numberss = [11, 22, 33, 44, 55, 66]

print(f"\n -This is the first element of the list: {numberss[0]}.\n -This is the last element of the list: {numberss[-1]}.")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4.b: Create a list with 6 elements (numbers). Print the 1st, 4th, and last elements.

           #💡 Explanation:
            # - In this task, you have to create a list of numbers.
            # - You have to print the first, fourth, and last elements of the list.
            # - You have to use print(), to print the elements.
            # - you use (\ n) to print the next line.


numbers = [1, 2, 3, 4, 5, 6]

print("\n", numbers[0], numbers[3], numbers[-1])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: Create a list of numbers. Then use [sum( )] and [len ( )] to print the average.

           #💡 Explanation:


numbers_1 = [11, 32, 45, 67, 87]
avg_num = sum(numbers_1) / len(numbers_1)

print(f"\n -The average number is: {avg_num}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                                                                # Hard level - examples.
# ➡️ Task 1: Create a String with a sentence. Reverse the string(from last character to first) and print it.

           #💡 Explanation:
                # - You can reverse strings using slicing [::-1]

sentence= "Hello Luis, how are you today? "

sentence_reverse = sentence[::-1]

print(sentence_reverse)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Create a list with numbers "from 1 to 10". Print only the {even numbers} using (list comprehension.)

           #💡 Explanation:

num_1 = list(range(1,11))

even_num = [number for number in num_1 if number % 2 == 0]
print (even_num)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2.b: Create a list with numbers from 1 to 10, using {for loop.}. Print the even numbers.


           #💡 Explanation:

number_3 = list(range(1, 11))

for number_3 in numbers:

    if number_3 % 2 == 0:

        print(number_3)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Create a dictionary {key-value pairs}. Add a new key-value, and delete one.

           #💡 Explanation:
                # -
                # 
                #  

person = {"name": "Luis", "age": 29, "work": "nurse"}
print(person)

person["new work"] = "Entrepeneur"

del person["work"]

print(person)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4: Create a list and convert it into a tuple. Then, try to modify the tuple(and show why it's not allowed)

           #💡 Explanation:

number_list = [1,2 , 3 ,4 ,5]
my_tuple = tuple(number_list)

print(my_tuple)

# my_tuple [2] = 4 -->  This is not posible
print(" You can modify tuples.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: Create two sets: {one with numbers 1 to 6} and {one with numbers 4 to 8}. Print intersection (common numbers)

           #💡 Explanation:


set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 7, 8}

common = set1.intersection(set2)
print(common)

set_mix = set1.union(set2)
print(set_mix)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6: Create a list of numbers and print the sum of all elements greater than 10.

           #💡 Explanation:
                # - Create a list of numbers
                # - We only sum() the numbers > 10.
                # - We use a { for loop } that check each number.

number_6 = [5, 12, 7, 10, 11]

sum_greater_10 = sum( n for n in number_6 if n > 10)
print(sum_greater_10)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 7: Create a dictionary with product names and prices. Loop through the dictionary and print: "The price of [product] is [price]."

           #💡 Explanation:

products = {"Workshop": 150, "Research": 1000, "behaviour in the company 6 month": 120000}

for product, price in products.items():
    print(f"\n -The price of {product} is {price} euros.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8: Create a nested dictionary with one person and inside it: name, age, contacts (with email and phone). Print the email.

           #💡 Explanation:

avatar_person = {
    "name": "Luis",
    "age": 29,
    "contact": {
        "email": "luis@ema.com",
        "phone": "112232424"
    }
}
print(f"\nEmail: {avatar_person['contact']['email']}")