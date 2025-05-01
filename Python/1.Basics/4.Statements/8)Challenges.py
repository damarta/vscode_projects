# # # --- ✅ Practice challenge ---

# #     # 👉 Asks the user for their age.

# # age = 29

# # if age >= 65:
# #     print("You are a senior.")
# # elif 18 <= age <= 64: 
# #     print("You are an adult.")
# # elif 13 <= age <= 17:
# #     print("You are a teenager.")  
# # else:
# #     print("You are a baby.")

# # # --- ✅ Practice challenge ---

# # menus = ["pizza", "pasta", "salad", "burger", "soup"]
# # for menu in menus:
# #     print(menu)

# # # --- ✅ Practice challenge ---
# # count = 0

# # while count < 10:
# #     print(count)
# #     count += 1 # timer

# # # --- ✅ Practice challenge ---
# # for number in range(0,100):
# #     if number == 50:
# #         continue
# #     print(number)

# # # --- ✅ Practice challenge ---
# # for number in range(1,12):
# #     print(number)
# # else:
# #     print("done!")
# # #########################################################


# # # --- ✅ Practice challenge ---


# #     # ➡️ Exercise 1 — Print numbers from 1 to 20:
# # for number in range(1,21):
# #     print(number)
    
# #     # ➡️ Exercise 2 — Print even numbers from 1 to 20:
# # for number in range(1,21):
# #     if number % 2 == 0:
# #         print(number)
        
# #     # ➡️ Exercise 3 — Print odd numbers from 1 to 20:
# # for number in range(1,21):
# #     if number % 2 != 0:
# #         print(number)
        
# #     # ➡️ Exercise 4 — Print numbers from 1 to 20, but skip the number 10:
# # for number in range(1,21):
# #     if number == 10:
# #         continue
# #     print(number)

# #     # ➡️ Exercise 5 — Print numbers from 1 to 20, but stop when you reach the number 15:
# # for number in range(1,19):
# #     if number == 15:
# #         break
# #     print(number)

# #     # ➡️ Exercise 6 — Print numbers from 1 to 20, but stop when you reach the number 15, then continue to the end:
# # for number in range(1,21):
# #     if number == 15:
# #         continue
# #     print(number)
# # else:
# #     print("done.")

# #     # ➡️ Exercise 7 — Print numbers from 1 to 20, but stop when you reach the number 15, then break out of the loop:
# # for number in range(1,21):
# #     if number == 15:
# #         break
# #     print(number)
# # else:
# #     print("done.")

# #     # ➡️ Exercise 8 - Print only even numbers from 2 to 20:
# # for number in range(2,21,2):
# #     print(number)
    
# #     # ➡️ Exercise 9 - Print only odd numbers from 1 to 19:  
# # for number in range(1,20,2):
# #     print(number)

# #     # ➡️ Exercise 10 - Print numbers from 20 to 1:
# # for number in range(20,0,-1):
# #     print(number)

# #     # ➡️ Exercise 11 - Print numbers from 20 to 1, but skip the number 10:
# # for number in range(20,0,-1):  
# #     if number == 10:
# #         continue
# #     print(number)
    
# #     # ➡️ Exercise 12 - Print numbers from 20 to 1, but stop when you reach the number 15:   
# # for number in range(20,0,-1):
# #     if number == 15:
# #         break
# #     print(number)

# #     # ➡️ Exercise 13 -  Print each letter of a word:
# # word = "My big dick"

# # for variable in word:
# #     print(variable)
 
# # #\\\\\\\\\/////////\\\\\\\\\\\\\\\\\\///////////////////////////\\\\\\\\\\\\\\///////////


# # #✅ 2️⃣ Practice: while loops

# #     #➡️ Exercise 1 — Count down from 10 to 1:
# # count = 100
# # while count > 0:
# #     print(count)
# #     count -= 1 # if you don't use this, become an infinite loop.

# # print("Lift off!")

# #     #➡️ Exercise 2 — Ask the user for a password until it's correct:
# # password = "dick"
# # attempt = ""

# # while attempt != password:
# #     attempt = input("Enter the password: ")
# # print("acess granted bitch!")

# #     #➡️ Exercise 2 — Ask the user to guess a secret number.
# # secret_num = 111
# # guess = 0

# # while guess != secret_num:
# #     guess = int(input("Guess the number bitch: "))

# # print("Is correct f*cker")


# #     #➡️ Exercise 3 — Keep asking until the user types "exit".

# # text = ""

# # while text != "exit":
# #     text = input("Type something (or type 'exit' to quit, but do you want to quite in life bro >:)?")
# #     print("You typed: ", text)

# #     #➡️ Exercise 4 — Countdown with a message at the end.

# # countdown = 5

# # while countdown > 0:
# #     print(countdown)
# #     countdown -= 1
# # print("💩")

# # # ✅ 3️⃣ Practice: combining for + while.

# # names = []
# # count = 0

# # while count < 5:
# #     name = input("Enter a name: ")
# #     name.append(name)
# #     count += 1

# # print("The names are: ")
# # for name in names:
# #     print(name)

# # # ✅ 4️⃣ MINI-PROJECT: “Number Guessing Game” 🎮
# # #         ⭐ Project instructions:
# #      # - The computer choosses a secret number between 1 and 20
# #      # - The user has to guess the number.
# #      # - After each guess, the program says if the guess is too high, too low, or correct.
# #      # - The game keeps looping until the correct guess.

# # import random

# # secret_number = random.randint(1,20)
# # guess = 0

# # print(" Welcome to the guessing game!")
# # print("I have chosen a number between 1 and 20. Can you guess it?")

# # while guess != secret_number:
# #     guess = int(input("Enter your guess: "))

# #     if guess < secret_number:
# #         print("Too low, try again!")
# #     elif guess > secret_number:
# #         print("Too high, Try again!")
# #     else:
# #         print("Correct! You guessed it! The secret number was {secret_number}.")

# # # ✅ 5️⃣ MINI-PROJECT: “Limited to 5 attempts” 🔐
# # import random

# # secret_number = random.randint(1,30)
# # guess = None
# # attempts = 0
# # max_attempts = 5

# # print("🎯 Welcome to the guessing game!")
# # print("I have chosen a number between 1 and 20. You have 5 attempts!")

# # while guess != secret_number and attempts < max_attempts:
# #     guess = int(input(f"Attempt {attempts + 1} of {max_attempts}: Enter your guess:"))
# #     attempts += 1

# #     if guess < secret_number:
# #         print("Too low, try again.")
# #     elif guess > secret_number:
# #         print("Too high, try again.")
# #     else:
# #         print(f"🎉 Correct! You guessed it! The number was {secret_number}.")
# #         print(f"🏆 You guessed it in {attempts} attempts!")
# # if guess != secret_number:
# #     print(f"🔒 Game over! The secret number was {secret_number}.")

# # # ✅ Step-by-step explanation:
# #     # 1️⃣ Import the random module.
# #     # 2️⃣ Generate a random number between 1 and 30.
# #     # 3️⃣ Initialize the guess and attempts variables.
# #     # 4️⃣ Set the maximum number of attempts to 5.
# #     # 5️⃣ Display a welcome message.
# #     # 6️⃣ Start a while loop that continues until the guess is correct or the maximum number of attempts is reached.
# #     # 7️⃣ Get the user's guess.
# #     # 8️⃣ Increment the attempts counter.
# #     # 9️⃣ Check if the guess is correct, too low, or too high.
# #     # 🔟 If the guess is correct, display a success message and the number of attempts.
# #     # 1️⃣1️⃣ If the guess is incorrect, display a failure message.
# #     # 1️⃣2️⃣ If the
# #     # 1️⃣3️⃣ If the maximum number of attempts is reached, display a game over message with the secret number.

# # ✅ 5️⃣ MINI-PROJECT: “Guessing game with difficulty levels.” 🔐

# import random

# print("🎯 Welcome to the guessing game!")
# print("I have chosen a number between 1 and 20.")

# #Ask for the difficulty level
# difficulty =  input("Choose difficulty: 'easy', 'medium', 'hard': ").lower()

# if difficulty == "easy":
#     max_attempts = 10
# elif difficulty == "medium":
#     max_attempts = 6
# elif difficulty == "Hard":
#     max_attempts = 3
# else:
#     print("Invalid difficulty level. Game over.")
#     max_attempts = 5

# # Generate a secret numbet
# secret_number = random.randint(1,20)
# guess = None
# attempts = 0

# print(f"You have {max_attempts} attempts. Good luck!")

# while guess != secret_number and attempts < max_attempts:
#     guess = int(input(f"Attempt {attempts + 1}: Guess the number: "))
#     attempts += 1

#     if guess < secret_number:
#         print("Too low, try again.")
#     elif guess > secret_number:
#         print("Too high, try again.")
#     else:
#         print(f"🎉 Correct! You guessed it! The number was {secret_number}.")
#         print(f"🏆 You guessed it in {attempts} attempts!")
# if guess != secret_number:
#     print(f"🔒 Game over! The secret number was {secret_number}.")

# ✅ 🎮 Replayable Guessing Game with Difficulty Levels.

import random

def play_game():
    print("\n🎯 Welcome to the guessing game with levels!")
    print("I have chosen a number between 1 and 20.")

    # ask for difficulty level
    difficulty = input("Choose difficulty: 'easy', 'medium', 'hard like my dick': ").lower()

    if difficulty == "easy":
        print("You only have 10 attempts.")
        max_attempts = 10
    elif difficulty == "medium":
        print(" You have 5 attempts")
        max_attempts == 5
    elif difficulty == "hard":
        print("You like hard baby 😈")
        max_attempts == 3
    else:
        print("You can not write like a normal persone stupid. I will give you more attempts for b*tch.")
        max_attempts == 11
    
    secret_number = random.randint(1,20)
    guess = None
    attempts  = 0

    print(f"You have {max_attempts} attempts. Good Luck p*shy")

    while guess != secret_number and attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Guess the size of my d*ck: "))
        except ValueError:
            print("⚠️ Pleae enter a valid number.")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"🎉 Correct! You guessed it! The number was {secret_number}.")
            print(f"🏆 You guessed it in {attempts} attempts!")
    if guess != secret_number:
        print(f"🔒 Game over! The secret number was {secret_number}.")

# --- 🎮 Game Loop : Add replay feature: ---
while True:
    play_game()
    replay = input("\n Would you like to play again? (Y/N): ").lower()
    if replay != "y":
        break
print("👋 Thanks for playing! Goodbye!")