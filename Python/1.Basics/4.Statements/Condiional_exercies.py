# ✅ Block — conditional.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1: Ask the user for their age. If age is greater than or equal 18, print "you are adult."

           #💡 Explanation
age = 29

if age >= 18:
    print("Yoou are adult")
else:
    print("You are a minor.")

print("Adult" if age >= 18 else "minor") # short way

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Ask for a number and print if it's positive or negative.

           #💡 Explanation
number_2 = int(input("Enter the number: "))

if number_2 >= 0:
    print("positief")
else:
    print("negatief")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Ask for a number and print if is positief, zero or negative

           #💡 Explanation
number_3 = int(input("Introduce a number: "))
if number_3 >= -1:
    print("Negative")
elif number_3 == 0:
    print("zero")
else:
    print("positive")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3.1: Ask two numbers, then review each number apart if it is negative, zero or positive. Then print the input and result.

           #💡 Explanation

number_11 = int(input("Introduce  the first  number: "))
number_22 = int(input("Introduce the second number: "))

if number_11 < 0:
    result_11 = "negative."
elif number_11 == 0:
    result_11 = "zero"
else:
    result_11 = "positive"

if number_22 < 0:
    result_22 = "negative"
elif number_22 == 0:
    result_22 = "zero"
else:
    result_22 = "positive"

print(f"The first number is {number_11} and the result: {result_11}")
print(f"The sencond number is {number_22} and the result: {result_22}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 4: Ask for a number.Check if it's between 10 and 50.

           #💡 Explanation

number_ex_4 = int(input("introduce a number: "))

if 10 >= number_ex_4 >= 50:
    print("is between ")
else:
    print("The number is greater than 10 and less than 50.")

number_ex_4a= int(input("introduce a number: "))
if number_ex_4a > 10 and number_ex_4a < 50:
    print("")
else:
    print("")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 5: Check if a number is either less than 0 or greater than 100

           #💡 Explanation
number_55 = int(input("enter a number"))

if number_55 < 0 or number_55 > 100:
    print("Number is outside the range 0-100")
else:
    print("Number is between 0 and 100")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 6 (Ternary Operator) : Write a program that ask for a temperature and print "hot" if above 30, "cool" if is otherwise. Using a Ternary operator

           #💡 Explanation
temperature = 18

print("hot" if temperature > 30 else "cool" )
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 7 (Nested if): Ask for number and check

           #💡 Explanation:
                # - if it's positive, check if it's even or odd.
                # - if it's negative, print "negative number"
ask_number1 = int(input("Introduce a number: "))

if ask_number1 > 0:
    if ask_number1 % 2 ==0:
       print("the number is positive and even")
    else:
        print("The number is positive and odd")
elif ask_number1 == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 7.1 (Nested if): Ask for number and check

           #💡 Explanation:
                # - if it's positive, check if it's even or odd.
                # - if it's negative, print "negative number"

number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 8.1:

           #💡 Explanation:

fruitt = input("Enter fruit name: ").lower()

if fruitt in ["apple", "banana", "mango"]:
    print("Available")
else:
    print("Not available") 

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 8 (check membership with condition): Ask for a fruit name. if it's in ["apple", "banana", "mango"], print "Available". Otherwise, print "No available."

           #💡 Explanation:
                # - 
                # - 

list_fruits = ["apple", "banana", "mango"]
print(f"Available fruits: {list_fruits}")

ask_user = input("Enter the name of a fruit to check if it's available: ").lower()

if ask_user in list_fruits:
    print(f"{ask_user.capitalize()} is available.") #  .capitalize() converts the first character to uppercase and the other characters to lowercase.
else:
    print(f"{ask_user.capitalize()} is not available.")




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 9 (using {not in} conditions): Ask the user if they are a member(yes or no). If not a member, print "Please sign up!"

           #💡 Explanation:

member = input("Are you a member? (yes/no): ").lower()

if not member == "yes":
    print("Please sign up!")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 10 (condition with String length): Ask for a user_name. If the user_name is less than 5 characters long, print "Too short.". Otherwise, print "Accepted."

           #💡 Explanation:

ask_user_name = input("Introduce your user name: (long than 5 characters)")

if len(ask_user_name) < 5:
    print("Too short!")
else:
    print("Accepted")