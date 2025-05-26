import json
import os
from habit import Habit

DATA_FILE = "habits.json"


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    return []


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


def main():
    habits = load_habits()

    print("\n📋 Your Habits:")
    for i, h in enumerate(habits):
        status = "✅" if h.done else "❌"
        print(f"{i+1}. {h.name} {status}")

    print("\nOptions:")
    print("1. Add habit")
    print("2. Mark habit as done")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        name = input("Enter habit name: ")
        habits.append(Habit(name))

    elif choice == "2":
        index = int(input("Enter habit number: ")) - 1
        if 0 <= index < len(habits):
            habits[index].done = True

    save_habits(habits)


if __name__ == "__main__":
    main()
