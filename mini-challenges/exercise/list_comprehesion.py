"""Traditional way(for loop)"""
result = []
for x in range(10):
    result.append(x*2)

# 💡 What this means:
    # result = [] -> Create an empty list.
    # for x in range(10) -> Loop over numbers 0 through 9.
    # result.append(x * 2) -> For each number x, multiply it by 2 and add it to the list.

# output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


""" THE PYTHONIC WAY (List Comprehension)"""
result = [x * 2 for x in range(10)]
# 💡 What this means:
# "For each number x in range(10), multiply it by 2, and collect it in a list."


"""Exercise 2: List comprehension with condition"""
result = [x * 2 for x in range(21) if x % 2 == 0]
