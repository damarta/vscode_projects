""" ----   Data Types   ---- """
# 1. Numeric Types
    # types:
        # Intenger: int()
            #operations with intengers

        # Float: float()
            # operations with floats
            # round()

        # complex (imaginary nunmber)
#----------------------------------------------------------------------------------

# Intenger: int()
    # - whole numbers( positive or negative ).
    # - no decimal point.

age = 18
age_user = 28
AGE_USER = 29

print(age)
print(age_user)
print(type(AGE_USER))
#----------------------------------------------------------------------------------


# Float: float()
price = 10.0
pi = 3.14159
negative_float = -12.5

print(type(price)) # you can know the <class>
# Floats are used fir precise calculations, currency, measurements or scientific data.

# use round( ) to fix problems with decimals:
    # syntax: round(number, ndigits)
                            # *ndigits = number of decimal places to round to
    # - If ndigits is not provided, python rounds the number to that many decimal places.
    # - If ndigits is omitted, Python rounds to the nearest whole number.
    # - The 2 in round( ..., 2 ) tells Python to round the result to 2 decimal places.
    # - This removes the extra unwanted digits.
print(round(0.1 + 0.2, 2))

# Another example:
number = 3.1424455

print(round(number))    # output : 3
print(round(number, 2)) # output : 3.14
print(round(number, 1))    # output : 3.1
print(round(number, 5)) # output : 3.14245
#----------------------------------------------------------------------------------

# Complex: float()
    #- Numbers with a real and imaginary part (used in advanced math)
    #- Written a + bj
number = 3 +4j