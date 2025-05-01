# ✅ Block — loops {while}.

            # while loop keeps repeating a block of code as long as a condition is {True}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1: Count from 1 to 10

           #💡 Explanation: Use a while loop to count from 1 until 10

            # - start with a number = 1
            # - While number <= 10, print it and add +1.

number = 1

while number <= 10:
    print(number)
    number += 1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Sum numbers until user enters 0

           #💡 Explanation: Ask the user for numbers and sum them until they type 0.

            # - keep asking for numbers
            # - Add to total
            # - Stop when user types 0.

total = 0
number = None

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number

print(f"The total sum is: {total}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task  3: Guessing game

#            #💡 Explanation: The user has to guess a secret number until they get right.

#             # - use a {while} until guess == secret.

secret_number = 10
guess = None

print("\nWelcome to the guessing game!")
print("\nTry to guess the number between 1 and 15.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Correct! 🎉 You guessed the number.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4: Countdown from 10 to 1

           #💡 Explanation: 

            # - start form 10
            # - print numbers until 1
            # - subtract one each time.

count = 10

while count > 0:
    print(count)
    count -= 1
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: Password check

           #💡 Explanation: 

            # - correct password = python123
            # - keep asking until user type it correctly

password_1 = "python123"
text = None

while text != password_1:
    text = input("Introduce the correrct password: ").lower()

    if text != password_1:
        print("incorrect")

print("Correct password.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6: Print only even numbers

           #💡 Explanation: 

            # - ask for numbers.
            # - if the number is even, print it.
            # - stop if user enters -1.

            #💡 step by step:
                # ask number
                # if even -> print it
                # if number = -1, stop.

number = None

while number != -1:
    number = int(input("Enter a number (if you write: -1 you stop): "))

    if number != -1 and number % 2 == 0:
        print(f"even number: {number}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 7: Multiplication table of 8

           #💡 Explanation: 
            # - start from 0
            # - print 8 * number
            # - increase  number each time until 12

           #💡 step by step:
            # - start i = 0
            # - print 8 * i.
            # - increase i by +1.
            # - stop at i = 11.

i = 0

while i <= 12:
    print(f"table of 8 -> 8 * {i} = {8 * i}")
    i += 1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8: Ask names until "exit"

           #💡 Explanation: 
                # - keep asking for names
                # - print each time.
                # - Stop if the user writes "exit"

           #💡 step by step:
                # - Ask for name
                # - print("Hello name")
                # - Stop if user types exit.


name = None

while name.lower() != "exit":

    name = input("Enter your name (type 'exit' to quit): ")

    if name.lower() != "exit":
        print(f"Hello, {name.capitalize()}!")  # we make sure that every first letter of the name is uppercase.
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 9: Print lines of stars

           #💡 Explanation: 
                # - Start with 1 star.
                # - Each time add 1 more star.
                # - stop when you reach 5.

           #💡 step by step:
                # - Start count = 1
                # - print count stars
                # - add 1
                # - Stop at 5

count = 1

while count <= 5:
    print("*" * count)
    count += 1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 10: Reverse a word

           #💡 Explanation: 
                # - Ask for a word.
                # - Start from the last letter and go backward.

           #💡 step by step:
                # - Ask for a word
                # - Start from las index (len(word) - 1).
                # - Print each letter backward.
                # - Decrease index by 1 each time.

word = input("Introduce one word: ").lower()

index = len(word) - 1

while index >= 0:
    print(word[index], end=" ")
    index -= 1

print(f"\nThe reversed word of '{word}' is above.")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
