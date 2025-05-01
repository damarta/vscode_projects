# ✅ Block — control flow loops.

            # What are exceptions?
                #- Exceptions are errors that happen while your program is running
                #- If you don't handle them, your program is running.
                #- We use {try/exept} blocks to catch and handle these errors without crashing the program.

                                                    # try:
                                                        # code that could cause a error
                                                    # except ErrorType:
                                                        # What to do if that error happens
                                                    # else:
                                                        #(optional) runs if no error happens
                                                    # finally:
                                                        # (optional) runs always, no matter what.



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1 (divide two numbers[handle division by zero])


            #💡 Explanation: 
                #- Ask the user for two numbers and divide them. Handle division by zero error.

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- Aks for twoo numbers
                #- User try/except to handle ZeroDivisionError.
                #- Print the result or an error message.

try:
    num_1 = int(input("Introduce the first number: "))
    num_2 = int(input("Introduce the second number: "))

    result = num_1 / num_2

    print(f"result: {result}")
except ZeroDivisionError:
    print("You can't divide by zero.")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# ➡️ Task 2 : Handle invalid input when asking for a number:


            #💡 Task: 
                #- Ask for a numbe and hadle the case when the user types text instead of a number

            #💡 Explanation: 
                #- We use int() to convert input into a number
                #- if the input is not a number (like a letter) python will raise a ValueError
                #- We use except ValueError: to catch this and show a message.

            #💡 step by step:
                #- ask for input
                #- try converting to int
                #- Cath ValueError.

try:
    n = int(input("Introduce a number: "))
    print(f"You entered {n}")
except ValueError:
    print("That was not a valid number")
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Safe list acess


            #💡 Task: 
                #- Access an index in a list and hadle if the index is out of range.

            #💡 Explanation: 
                #-  Index : in python, when you have a list [or string], each item has a position called an index. Star counting from 0.
                #- IndexError: This happens when your ask for a position (index), that doesn't exits in the list
                #- ValueError: This happens when python expects a number, but the user types something else.

            #💡 step by step:
                #- Creaate a list
                #- Ask for an index
                #- Handle IndexError

my_list = [10, 20, 30]

try:
    index = int(input("Enter index (0-2): "))
    print(my_list[index])
except IndexError:
    print("index out of the range.")
except ValueError:
    print("Invalid index. Must be a number")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 4: Catch multiple exceptions (valueError and ZerroDivisionError)

            #💡 Task: 
                #- Ask the user for two numbers.
                #- try to divide them
                #- Handle both Errors: 
                    # if the second number is a 0 
                    # if the user types something that's not a number.

            #💡 Explanation: 
                #- ZeroDivisioError happens when trying to divide by zero
                #- ValueError happens when trying tto convert textt into a number.
                #- We can hadle both with two separete except blocks

            #💡 step by step:
                #- Ask for the first number and convert to float.
                #- ask for the second number and convert to float
                #- Try to divide a / b
                # if b= 0, catch ZeroDivisionError and print an error.
                #- if the user enter letter, catch ValueError and printan Error.
                #- Otherwise, print the result.

try:
    a = float(input("Introduce the first number: "))
    b = float(input("Introduce the second number: "))
    result = a / b
    print(f"\nThe result is: {result}")
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("\nThe value is not correct!")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 5 ) Handling FileNotFoundError


            #💡 Task: 
                #- Try to open a file called, data.txt and read it
                #- if the file doesn't exist, catch the error and show a friendly messahe.
 

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- - Use with open("data.txt", "r") to try to open the file.
                #- If the file exists, read its content and print it.
                #- If the file does not exist, Python raises a FileNotFoundError.
                #- The Except FileNotFoundErrorn block catches that and shows a message.



try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6) Handling Multiple Exceptions in one program


            #💡 Task: 
                # ask the user for two numbers
                # Try to divide them
                # Try to open a filled called data.txt and print its content.
                # Cath and handle
                    # ValueError
                    # ZeroDivisionError
                    # FileNotDoundError

            #💡 Explanation: 
                #- 

            #💡 step by step:
                # Ask the user for two numbers (using float()).
                # Use try to divide the numbers.
                # If somethinf goes wrong, hadle it.
                # if succesful, try to open

try:
    # ask for the numbers
    a = float(input("Introduce the first number: "))
    b = float(input("Introduce the second number: "))

    # Division of the numbers
    result = a / b
    print(f"The division is: {a} / {b} = {result}")

    #  Try to open a file and read a file
    print("\nAttempting to read 'data.txt' ...")
    with open("data.txt", "r") as file:
        content = file.read()
        print("Document 'datat.txt'\n", content)

except ValueError:
    print("The value is incorrect.")
except ZeroDivisionError:
    print("You can not divide by zero.")
except FileNotFoundError:
    print("This file don't exist.")

finally:
    print("End of the program.")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
















# ➡️ Task 


            #💡 Task: 
                #- 

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>