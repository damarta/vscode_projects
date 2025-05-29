# Main Streamlit app

import streamlit as st
import json
import os
from habit import Habit

DATA_FILE = "habits.json"


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(item) for item in data]
    return []


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


def main():
    st.title("Habit Tracker App")

    habits = load_habits()

    st.header("Your Habits")

    for i, habit in enumerate(habits):
        done = st.checkbox(habit.name, value=habit.done, key=f"habit_{i}")
        if done != habit.done:
            habits[i].done = done
            save_habits(habits)
            st.rerun()

    new_habit_name = st.text_input("Add a new habit")
    if st.button("Add Habit") and new_habit_name.strip():
        new_habit = Habit(new_habit_name)
        habits.append(new_habit)
        save_habits(habits)
        st.rerun()


if __name__ == "__main__":
    main()
