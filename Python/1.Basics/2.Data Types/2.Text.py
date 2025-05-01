""" ----   Data Types   ---- """

# 2. Text 
    # types:
        # string: str(): What is a string?
        # String indexing
        # String slicing
        # String Operations:
            # Concatenation
            # Repetition
            # membership (in, not in)
        # String Methods (common Functions)
        # String Formatting
        # Escape Characters
        # String Immutability
        # Useful String Functions

        
"""1. What is a String?"""
# A string (str) is a sequence of characters (letters, numbers, symbols) enclosed in quotes.
# Example 1.
name = "Luis"
message = "Hello, world!"
print(type(name), type(message))
print(name, message)

#--------------------------------------------------------------------------------------------

""" 2. String Indexing ( Accessing Characters. )"""
# Strings are sequence of characters, and each character has a position (index).
# Start in 0 until the last word; example: H E L L O [0,4]
text = "Hello Luis"
print(text[:])
print(text)