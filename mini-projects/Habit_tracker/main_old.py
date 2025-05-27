""" This file is the logic that controls the app."""

# 💬 What this means: this imports the JSON module -> json.dump() -> save data to file // json.load() ->load data from a file
import json

# 💬 What this means: This give acess to operating system functions. You check if the file exists. This prevents error when the file isn't there yet.
import os

# 💬 What this means: this import the { Habit class } from your habit.py file.
from habit import Habit


# 💬 What this means: This create a constant variable that defines your file name.
DATA_FILE = os.path.join(os.path.dirname(__file__), "habits.json")

# -- step 1: Load JSON data --


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    return []
   # 💬 What this means:
   # - If habits.json exists → open and read it.
   # - Use Habit.from_dict() to convert raw JSON into real objects.
   # - If the file doesn’t exist → return an empty list

# -- step 2: Save to JSON --


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)
   # 💬 What this means:
   # - Loop over every habit → convert it to dict → save to file
   # - indent=2 make the file readable

# -- Step 3: Start the APP


def main():
    habits = load_habits()
    # 💬 What this means:
    # - this start your program.
    # - it loads all previously saved habits from the Json file (like opening a saved file)
    # - you now have a list of 'Habit' objects stored in the variable 'habits'.

    print("\n📋 Your Habits:")
    for i, h in enumerate(habits):
        status = "✅" if h.done else "❌"
        print(f"{i+1}. {h.name} {status}")
    # 💬 What this means:
    # - show habits and their status
    # - f"{i+1}" = display-friendly index (starts at 1, not 0)

    print("\nOptions:")
    print("1. Add habit")
    print("2. Mark habit as done")
    print("3. Exit")
    choice = input("> ")
    # 💬 What this means:
    # - Ask user what they want to do

# -- Step 4: Add habit
    if choice == "1":
        name = input("Enter habit name: ")
        habits.append(Habit(name))
        # 💬 What this means:
        # - create a new Habit() and add it to the list.

# -- step 5: Mark as done
    elif choice == "2":
        index = int(input("Enter habit number: ")) - 1
        if 0 <= index < len(habits):
            habits[index].done = True
        # 💬 What this means:
        # - ask for a number (1-based), convert to list index(0-based)
        # - Subtract 1 because Python lists start at index 0
        # - set done = True for that habit


# -- Step 6: save the changes --
    save_habits(habits)
    # 💬 What this means:
    # - This writes all your updated habits (with .to_dict()) into the habits.json file
    # - It saves everything the user just did


# -- Step 7: Run Automatically
if __name__ == "__main__":
    main()
    # 💬 What this means:
    # - This tells Python: “Only run main() if this file is being run directly (not imported).”
