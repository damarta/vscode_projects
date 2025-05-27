""" This file is the logic that controls the app."""
import json
import os
from habit import Habit

DATA_FILE = os.path.join(os.path.dirname(__file__), "habits.json")

# -- step 1: Load JSON data --


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    return []


# -- step 2: Save to JSON --
def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


# -- Step 2.A: Genetpr with yield: Get only incomplete habits
def get_incomplete(habit_list):
    for h in habit_list:
        if not h.done:
            yield h


# -- Step 3: Start the APP
def main():
    habits = load_habits()

    print("\n📋 Your Habits:")
    # Comprehension-based habit display
    [print(f"{i+1}. {h.name} {'✅' if h.done else '❌'}")
     for i, h in enumerate(habits)]

    # Optional: show incomplete using generator
    print(f"\n❌ Incomplete habits: ")
    for h in get_incomplete(habits):
        print(f"🔸 {h.name}")

    print("\nOptions:")
    print("1. Add habit")
    print("2. Mark habit as done")
    print("3. Exit")
    choice = input("> ")

# -- Step 4: Add habit
    if choice == "1":
        name = input("Enter habit name: ")
        habits.append(Habit(name))

# -- step 5: Mark as done
    elif choice == "2":
        index = int(input("Enter habit number: ")) - 1
        if 0 <= index < len(habits):
            habits[index].done = True

    # Bonus: filter() + lambda to get incomplete list
    incomplete = list(filter(lambda h: not h.done, habits))
    for h in incomplete:
        print(f"🔹 {h.name}")


# -- Step 6: save the changes --
    save_habits(habits)


# -- Step 7: Run Automatically
if __name__ == "__main__":
    main()
