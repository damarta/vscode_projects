# == Imports ==
import streamlit as st
from habit import Habit
import json
import os


# == File path for saving data ==
DATA_FILE = os.path.join(os.path.dirname(__file__), "habits.json")


# == Load habits from JSON file ==
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    return []


# == Save habits to JSON file ==
def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)


# == 🚀 Streamlit UI Starts ==
st.title("📋 Habit Tracker (Streamlit Version)")
st.caption("Track your daily habits and mark them as done ✅")
st.markdown("---")

habits = load_habits()

# == ✅ Show all habits ==
st.subheader("✅ Your Habits")
for i, h in enumerate(habits, start=1):
    status = "✅" if h.done else "❌"
    st.markdown(f"**{i}. {h.name}** - {status}")

# == ❌ Show only incomplete habits ==
incomplete = [h for h in habits if not h.done]
if incomplete:
    st.markdown("---")
    st.subheader("🔁 Incomplete Habits")
    for h in incomplete:
        st.write(f"🔶 {h.name}")

# == ➕ Add new habit section ==
st.markdown("---")
st.subheader("➕ Add New Habit")

new_habit = st.text_input("Enter a new habit")

if st.button("Add habit") and new_habit.strip():
    habits.append(Habit(new_habit.strip()))
    save_habits(habits)
    st.success("Habit added!")
    st.experimental_rerun()  # type: ignore  ✅ Optional warning suppressor
