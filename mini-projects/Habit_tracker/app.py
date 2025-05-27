import streamlit as st
from habit import Habit
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "habits.json")


def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    return []


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


# 🚀 Streamlit UI Starts Here
st.title("📋 Habit Tracker (Streamlit Version)")
habits = load_habits()

# ✅ Show habits
st.subheader("Your Habits")
for i, h in enumerate(habits):
    st.write(f"{i+1}. {h.name} {'✅' if h.done else '❌'}")

# ➕ Add habit
new_habit = st.text_input("Add a new habit")
if st.button("Add Habit"):
    habits.append(Habit(new_habit))
    save_habits(habits)
    st.experimental_rerun()

# ✅ Mark as done
habit_to_mark = st.number_input(
    "Mark habit as done (number)", min_value=1, max_value=len(habits), step=1)
if st.button("Mark as Done"):
    index = habit_to_mark - 1
    habits[index].done = True
    save_habits(habits)
    st.experimental_rerun()
