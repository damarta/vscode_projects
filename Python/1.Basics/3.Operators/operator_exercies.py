# ✅ Block — Operators.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 1( Arithmetic - addition): Create two numbers and add them.

           #💡 Explanation

x = 8
y = 2
z = 1

result = x + y + z
print(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 2 (Assignment): Start with s = 10, then increase by 5 using += and print the result.

           #💡 Explanation

s = 10
s += 5

print(s)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 3(Comparison): Check if two numbers are equal ussing == and print True or False.

           #💡 Explanation:
                # - the == operator compares if values are the same.

aa = 10
bb = 30

print( aa == bb)

# ➡️ Task 4.a: Use {and} to check if a number is greater than 5 and less than 20.

           #💡 Explanation:
                # - Both conditions must be True.

number_T = 15

if number_T > 5 and number_T < 20:
    print("-True")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 4.b: Use {and} to check if a number is greater than 5 and less than 20.

           #💡 Explanation:
                # - Both conditions must be True.

number_s = 12
print( number_s > 5 and number_s < 20)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 5: Create two variables with the same value but different objects. Check if they are the same object

           #💡 Explanation:
                # - {is} checks if both refer to the exact same object in memory.

aa = [2, 4, 5]
bb = aa

print(aa is bb) # The are the same.

cc = [1, 2, 3]
dd = [1, 2, 3]

print(cc is dd) # [the have the same content but different memory]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 6: Check {if} a word 'apple' is present {in} a list of fruits

           #💡 Explanation:
                # - {in} check if something is inside a collection.

list_fruit = ["apple", "pera", "banana"]

print("aaple" in list_fruit)
print("apple" in list_fruit)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 7: Use the modulus operator {%}, to find the remainder when diving 37 by 6.

           #💡 Explanation:
                # -
div_1 = 37
div_2 = 6

result_1 = div_1 % div_2
print(result_1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 8: Check if a number is either {less than 0} or {greater than 100.

           #💡 Explanation:
                # -

num_8 = 101

print(num_8 < 0 or num_8 > 100)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 9: Assign one variable to another and use {is} to prove they are the same object.

           #💡 Explanation:
                # - if two variables point to the same object, is will return True.
a1 = [1, 2, 3]
b1 = a1

print(b1 is a1 and a1 is b1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # <<<< ADVANCED >>>>>

# ➡️ Task 1: calculate the result of this formula: ((5 + 3)* 2)** 2 /4 and print it.

           #💡 Explanation:
                # - Floow the math order: parentheses -> multiplication -> exponent -> division

formula_1 = ((5 + 3)*2)**2 / 4
print(formula_1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 2: Start with [x = 50]. subtract 10, multiply 2, then fivide by 4, using combined assignment operators.

           #💡 Explanation:
                # -
xx = 50
xx -= 10
xx *= 2
xx /= 4

print(xx)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 3: Check {if} 5 < 10 < 20 in one line.

           #💡 Explanation:
                # - Python allows chained comparison.
zz = 5 < 10 < 20
print(zz)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 4: Check if a number is either between 10 and 20 {or} equal to 100

           #💡 Explanation:
                # -
qq =100

print(10 < qq < 20 or qq == 100)
print((10 < qq < 20) or (qq == 100)) # clean option

#>>>>>>>>>>>>>>>>>>>>>>>>>>d>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 5: Check if a list {is not} empty

           #💡 Explanation:
                # -
list_empty = [1, 2, 3]

print(list_empty is not "" )
print(not not list_empty) # best option
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 6: Check if "py"  {is in}  "Python programming".

           #💡 Explanation:
                # -
python_va = "Python programing"

print("py" in python_va.lower()) # True
print("py" in python_va)         # False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 7: Check if two different list are not the same object

           #💡 Explanation:
                # -

list_a = ["luis"]    
list_b = ["luis"]  #  same values, but different object.

print(list_a is not list_b)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ➡️ Task 8: Write a short code that prints if a number is [even] or [odd] {using %}.

           #💡 Explanation:
                # -
numb_short = 2

if numb_short % 2 == 0:
    print("even")
else:
    print("odd")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ➡️ Task 9: Use {&} on two numbers and print the result.

           #💡 Explanation:
                # - {&} = bitwise AND
                # - Performs AND at binary level.

a_bitwise = 5
b_bitwise = 2

print(a_bitwise & b_bitwise)                 
#>>>>>>>>>>>>>>d>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
