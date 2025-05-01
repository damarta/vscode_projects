# ✅ Block — control flow loops.

            # What is loop control flow?
               # - you can stop them early
               # - Skip certain steps.
               # - Or add logic for when the loop ends.

          # Keywoords in loop control flow:
               # - break (stop the loop immediately)
               # - Continue (skip the current iteration and move to the next)
               # - pass (do nothing [used as a placeholder])
               # - else in loop (runs only if the loop finishes without hitting a break.)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# ➡️ Task 1 (Stop counting at 7 {break}): Count numbers from 1 to 10, but stop when the number reaches 7

           #💡 Explanation: 
               # - Start counting from 1
               # - When the number reaches 7, stop the loop.
               # - break tells Python to stop the loop right away.

           #💡 step by step:
               # - start with i = 1
               # - if i == 7, stop printing (break)
               # - otherwise print the number and add 1.
i = 1

while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1
            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 2 (skip mutiple of 3 (continue)) : Print numbers from 1 to 15, but skip those divisble by 3

           #💡 Explanation: 
               # - If a number is divisble by 3, use continue to skip printing it.

           #💡 step by step:
               # - Start from 1
               # - while loop that counts until 15
               # - if number % 3 == 0, use conitnue to skip
               # - Otherwise, print the number

i = 1

while i <= 15:
    if i % 3 == 0:
        i += 1 # += is for the condition ; we add += 1 first so that it goes to the next numbers if is % 3 ==0 continue
        continue
    print(i)
    i += 1 # The second += is for the variable from the loop. if is not divisible by 3, we print the number + increase i += 1.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 3 (The Guessing game using break): Ask the user to guess a secret number.

           #💡 Explanation: 
               # - if the guess is correct, show a success message and stop the loop
               # - if it's wrong, ask again until the user gets it right.

           #💡 step by step:
               # - define the secret number
               # -Start an infinite loop
               # - Ask the user to guess
               # - check if the guess is correct.
               # - if not correct, show a retry message.

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Introduce the secret number: "))
    if guess == secret_number:
        print("Correct password!")
        break
    else:
        print("The password is correct.")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4 (print Only odd numbers (use continue)):

           #💡 Explanation: 
               # - Print numbers from 1 to 20, skiping all even numbers
               # - Skip any number divisible by 2 (even)

           #💡 step by step:
               # - Start from 1
               # - If even skip, skip with continue
               # - If odd, print it.
    
i = 1

while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(f"The odd number is: {i}")
    i += 1


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 5 (Stop asking for names on "stop" input):

#            💡 Explanation: 
                # - Keep asking for names, stop when the user types 'stop'
                # - If input equals stop, exit the loop

#            💡 step by step:
                # - ask for input
                # -if input is stop, break
                # - Otherwise, greet
print("\nWelcome, introduce your name to start the code or write 'stop' to exit")
while True:
    name = input("\nEnter your name: ")
    if name.lower() == "stop":
        print("\nSee you next time :)")
        break
    else:
        print(f"\nWelcome, {name.capitalize()}. Nice to see you again :) .")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6 (Print Stars but stop at 4 stars (break) )

            #💡 Explanation: 
                #- Print increasing lines of stars but stop after 4 stars.
                #- Stop when lines has 5 stars

            #💡 step by step:
                #- Start count = 1
                # - Print * X count
                # - If count == 5, break

i = 1

while i <= 10:
    if i == 5:
        break
    print("*" * i)
    i += 1
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 7 (Skip multiple of 4 in counting)

            #💡 Explanation: 
                #- Skip numbers divisible by 4 using continue

            #💡 step by step:
                #- count from 1 to 20
                #- if divisible by 4, skip
                #- Otherwise, print.

i = 1

while i <= 20:
    if i % 4 == 0:
        i += 1
        continue
    print(i)
    i += 1


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8 (Stop asking numbers after negative input)

            #💡 Explanation: 
                #- Ask the user for numbers, stop when they enter a negative number.
                #- Break the loop wheninput <0.

            #💡 step by step:
                #- ask for a number
                #- if < 0, break
                #- Otherwise print

while True:
    number = int(input("Introduce numbers: (if number is negative 'stop')"))
    if number < 0:
        print(f"\nThis numbers is negative, the code stop: {number}")
        break
    print(f"Positive number :{number}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 9 ( Print numbers skipping multiples of 5)

            #💡 Explanation: 
                #- print from 1 to 50 b ut skip multiples of 5
                #- skip numbers divisibles by 5

            #💡 step by step:
                #- loop from 1 to 50
                #- if divisible by 5, continue
                #- Else print

i = 1

while i <= 50:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 10 (Multiplication table of 7( Stop at result >50))

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- 

i = 1

while True:
    result = 7 * i
    if result > 50:
        break
    print(f"7 X {i} = {result}")
    i += 1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>s>>>>>>>>>>>>>>>>>>>>>>>>>>


                        #✅ Loop Control Flow: pass and else
# ➡️ Task 1 (pass: Create a loop that checks numbers from 1 to 5, and when the number is 3, do nothing and continue with the rest)

            #💡 Explanation: 
                #- keyword pass does nothing
                #- it's used as a placeholder when you need to write block of code but haven't decided what to put there yet.
                #- The program will not stop. It will just skip that point and continue

            #💡 step by step:
                #- loop from 1 to 5
                #-  when the number is 3, do nothing (use pass)
                #- Print the other numbers.


i = 1

for i in range (0,6):
    if i == 3:
        pass
    else:
        print(i)

i = 1

while i <= 5:
    if i ==3:
        i +=1
        print(i)
        pass
    print(i)
    i += 1

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 2 (Else in loops (Loop through numbers from 1 to 5. After the loop finishes successfully (without a break) print "Loop completed"))

            #💡 Explanation: 
                #- The Else block in a loop runs only if the loop is not stopped by a break.
                #- Its a great to use when you want to confirm that the loop finished fully.
            

            #💡 step by step:
                #- Start a loop from 1 to 5
                #- Print each number
                #- After the loop finishes, the else block runs and prints a message.

block = 1

while block <= 5:
    print(i)
    i += 1
else:
    print("Code completed")



for block in range(1,6):
    print(block)
else:
    print("Done!")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ➡️ Task 

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

























# ➡️ Task 

            #💡 Explanation: 
                #- 

            #💡 step by step:
                #- 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
