# ✅ Block — loops {for}.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1: Print numbers from 1 to 10

           #💡 Explanation:
            # - Use a for loop to print numbers from 1 to 10

for number in range(1,11):
    print(number)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2: Sum of numbers from 1 to 100

           #💡 Explanation:
                # -Use a for loop to calculate and print the sum of numbers of 1 to 100.
                # - Create a variable with 0 value.
                # - use for in range
                # - add the sum to the total every time the loop goes to a new number and add a new one.
                # - Print.

total = 0

for i in range (1,101):
    total += i 

print(total)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3: Print even numbers between 1 and 50.

           #💡 Explanation:
                # - Print only the even numbers between 1 and 50.
                # - Even numbers are divided by 2. 
                # - You start with (2,) because is between 1 and 50, but 1 is not even, you need to start with 2.
                # - You can use range(2, 51, 2) to jump by two steps and get even numbers directly.
                # range( , ,2) tell to python than you want even numbers.

for i in range(2, 51, 2):
    print(i)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4: Print multiplication table of 5

           #💡 Explanation:
                # - Print the multiplication table for 5.
                # - Multiply 5 by numbers from 1 to 10
                # - use f"string" for clear output.

for i in range(1,11):
    print(f" 5 x {i} = {5*i}")

for a in range (0,11, 2):
    print(f"5 X {a} = {5*a}")    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 5: Print charactes of a word.

           #💡 Explanation:
                # -  Ask for a word and print each letter.
                # - The for loop can go through each letter in a string.
                # - Create a variable with a input; this input will be a string. Ask to the user for this string.
                # - Use loop {for} to print each letter. For this you need to create a 'new variable' + use {in} and the variable you used before. Using {in} python understand that he need to print each letter of this word.
                # - And least, print.

word = input("Introduce a word for print each letter of the string: ")

for letter in word:
    print(letter)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6: Find factorial of a number.

           #💡 Explanation:
                # - What is a factorial? :
                    # - The factorial of a number [n](written as {n!}) is the product of all positive intengers form 1 to n.
                    # example:
                        #    5! = 5 * 4 * 3 * 2 * 1 = 120
                        #    0! = 1 ; (is defined as 1 by definition)
                     
                # - Calculate the factorial (multiplying all numbers up to that number.)
                # - Start with factorial = 1
                # - multiply facotrial by each number in the loop.

                # First ask, the user to enter a number. use int() to have a whole number.
                # store this number in n
                # Create a Variable called factorial and start at 1, because any multiplication by 0 would erase the result, and multiplying by 1 is safe.

                # This loop goes from 1 to n (remeber that range stops before the last number, so we use n+1).
                # Each time, it multiplies the current value of factorial by i.
                # Example if {n} = 4
                        # Start: factorial = 1
                        # formula: factorial * i

                        # i = 1 -> 1 * 1 = 1
                        # i = 2 -> 1 * 2 = 2
                        # i = 3 -> 2 * 3 = 6
                        # i = 4 -> 6 * 4 = 24
                          

                # This print the final result with a clear message.
                    # print(f"the Factorial of {n} is {factorial}")
                              
            #✅ What happens if the user enters 0?
                # The loop won't multiply anything, factorial stays at 1, which is correct (by definition, 0! = 1).

n = int(input("Enter the number: ")) 
factorial = 1

for i in range (1, n+1):
    factorial *= i

print(f"The Factorial of {n} is {factorial}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 7: Sum of odd numbers between 1 and 100

           #💡 Explanation:
                # - use range(1, 100+1, 2) to take only odd numbers (steps of 2 starting at 1).

                # ✅ How does range(1, 101, 2) work?
                    # range(start, stop, step)
                # ✅ Example (visualizing the sum):
                    # the loop does:
                    # 0 + 1 = 1
                    # 1 + 3 = 4
                    # 4 + 5 = 9
                    # 9 + 7 = 16 
                    # . . . all the way until 100

total_1 = 0

for i in range(1, 101+1, 2):
    total_1 += i

print(total_1)

#✅ Want to make it more visual?
total_2 = 0
    
for i in range(1, 101+1, 2):
    total_2 += i
        # formula: total_2 + i
        # 0 + 1 (until 101)
    print(f" Added {i}, current sum is {total_2}")

print(f"The final sum of odd numbers is {total_2}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8: Count vowels in a sentence

           # 💡 Explanation: The goal is ask the user to write a sentence and count 'how many vowels are in that sentence. (a, e, i, o, u)

                 # - Loop through each letter.
                 # - Check if the letter is {in} a, e, i, o, u.
                 # - if is yes, add 1 to the count.

                 #  1. sentence = input("").lower()
                        # we ask the user to type any sentence.
                        # .lower() makes the sentence all lowercase, so we don't miss capital letters (like A or E).
                 #  2. Vowels = "aieou"
                        # we store all the vowels in a string.
                        # This make it easy to check: is the current letter inside this string?
                 #  3.  Count = 0
                        # we start with a count of zero.
                        # each time we find a vowel, we will add 1 to this count.
                 #  4. The loop:
                        # we go through each letter in the user's sentence.
                        # For each letter, we ask: is this letter in the vowels list?
                        # if yes, add 1 to count.

sentence = input("Introduce a sentence: ").lower()

vowels = "aeiou"

count = 0 

for letter in sentence:
    if letter in vowels:
        count += 1

print(f"Number of vowels: {count}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8.1

#           💡 Explanation:
#                - 

sent = input("Introduce a sentence: ").lower()

consonats = "hlyns"
found_consonats = []
count = 0

for letter in sent:
    if letter in consonats:
        count +=1
        found_consonats.append(letter)


print(f"The number of consonats is : {count}")
print(f"Consonats found: {', '.join(found_consonats)}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 9: Print a square of stars

            # 💡 Explanation: Goal print a square with *

                  # 1. Ask for size.
                  # 2. We use a {for loop} that runs size time(one for each line).
                  # 3. Inside the loop, we print * Repeated size times using * size.
                  # 4. Each loop prints one row of stars.

            
            # ✅ Detailed explanation of the code:

                            #-- {code} --
                    # size = int(input("Enter the size of squares: ")) output: 4 

                    #   👉 Here you ask the user for a number. This number will define:
                        #- if the user put 4. this means it's 4 * 4
                        #- How many rows your square has (line)
                        #- How many starts will be in each row.

                        #-- {code} ---
                    
                        # for i in range(size)
                        #   print("*" * size)

                    #   👉 What happens here:
                        #for i in range(size):
                            # - this means:"Repeat the following action size times" (for each row).
                        #print("*" * size)
                            # - The * operator with strings repeats that character.
                            # - example: "*" * 4 will print{****}
                            # - so for each row, it prints size numbers of stars.
            # ✅ Visual diagram:
                # i = 0 -> action -> print 4 starts(*) -> ****
                # i = 1 -> action -> print 4 starts(*) -> ****
                # i = 2 -> action -> print 4 starts(*) -> ****
                # i = 3 -> action -> print 4 starts(*) -> ****

size = int(input("Enter the size of squares: "))

for i in range(size):
    print("*" * size)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 9.1

#           💡 Explanation:
#                - 
sizee = int(input("Enter the size of the square: "))

for i in range(1, size + 1):
    print(f"Row {i}: {"*" * sizee}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 9.2 Print a triangle with *

#           💡 Explanation: Ask the user  for a size and print a right-angled tiangle using *
               # - The loop runs from 1 to size +1
               # - each time, we print i stars.
               # - First line: 1 star, second line: 2 stars, and so on.

sizeee = int(input("Enter the size of the triangle: "))

for i in range(1, sizeee + 1):
    print("*" * i)



# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 10: Sum of numbers from user input

            #💡 Explanation: Ask the user 5 numbers and print their sum.

                # - We start with a variable total = 0 to store the sum.
                # - We use a for loop that runs 5 times (because we want 5 numbers.)
                # - Each time, we ask the user to input a number (convert it to intenger.)
                # - We add that number to the total ( totaal += number).
                # - after the loop ends, we print the totaal sum.


totaal = 0

print("\nIntroduce 5 numbers:")

for i in range(5):
    number = int(input("\n-Enter a number: "))
    totaal += number

print(f"\nThe sum is {totaal}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 11. Hollow square of stars.

#          💡 Explanation: A square made of *, but with empty space (no stars) inside.
#               - {code}
#                    if row == 0 or row == -1
#                        - For the first and last row, print a full line of starts
#                    else:
#                       - print one star, then space (" " * (sizes *2)), then another star.
                    

sizes = int(input("Enter the size of the hollow square: "))

for row in range(sizes):
    if row == 0 or row == sizes -1:
        print("*" * sizes) # First and last rows are full of stars.
    else:
        print("*" + " " * (sizes - 2) + "*") # in the middle rows, starts only at the begging and end.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 12. Pyramid of stars

#           💡 Explanation: triangle that grows centered, like this (for size = 5):

                # - the number of stars on each row follows this pattern:
                # - 2 * row - 1
                # row 1 = 1 star
                # row 2 = 3 star
                # row 3 = 5 stars, and so on.

                # The spaces line adds spaces in front to make it centered.


size = int(input("Enter the size of the pyramid: "))

for i in range(1, size + 1):

    spaces = " " * (size - 1)  # Add spaces before starts to center them
    starts = "*" * (2 * i - 1) # Calculates how many starts for each row.

    print(spaces + starts)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>








