from habit import Habit

habits = [
    Habit("Walk with the dogs", True),
    Habit("Stretch", False),
    Habit("Read", False),
    Habit("Hydrate", False),
    Habit("Last walk", False),
]
incomplete = [h for h in habits if not h.done]
# 💬 What this means:
# - “Loop over all habits, and only keep the ones where done is False.”

for h in incomplete:
    print(h.name)

    # Turn the list in a dictionary comprehension to create a output:
habit_status = {h.name: h.done for h in habits}
# print(habit_status)

# Turn the list a dictionary with condition:
habit_condition = {h.name: h.done for h in habits if not h.done}
# print(habit_condition)


# Unique words from a list
habit_names = [
    "Read",
    "Stretch",
    "Read",         # duplicate
    "Meditate",
    "Stretch",      # duplicate
    "Hydrate"
]
unique_habits = {name for name in habit_names}
# print(unique_habits)

# Extract the first letter of each unique habit name.
name = [0]
first_letters = {name[0] for name in habit_names}
# print(first_letters)

upper_cased = list(map(lambda name: name.upper(), habit_names))
print(upper_cased)
