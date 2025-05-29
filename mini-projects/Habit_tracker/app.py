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

    priority_colors = {"red": "🔴", "orange": "🟠", "green": "🟢"}

    for priority in ["red", "orange", "green"]:
        st.subheader(
            f"{priority_colors[priority]} {priority.title()} Priority Habits")
        for i, habit in enumerate([h for h in habits if h.priority == priority]):
            # checkbox, name, edit, delete
            cols = st.columns([0.05, 0.7, 0.1, 0.1])
            done = cols[0].checkbox("", value=habit.done,
                                    key=f"{priority}_done_{i}")
            if done != habit.done:
                habit.done = done
                save_habits(habits)
                st.rerun()

            # Initialize edit_mode dict if not exists
            if 'edit_mode' not in st.session_state:
                st.session_state.edit_mode = {}

            edit_key = f"{priority}_{i}"

            if st.session_state.edit_mode.get(edit_key, False):
                new_name = cols[1].text_input("Edit Habit Name", value=habit.name,
                                              key=f"{priority}_name_input_{i}")
                if cols[2].button("Save", key=f"{priority}_save_{i}"):
                    if new_name.strip():
                        habit.name = new_name.strip().title()
                        save_habits(habits)
                        st.session_state.edit_mode[edit_key] = False
                        st.rerun()
                if cols[3].button("Cancel", key=f"{priority}_cancel_{i}"):
                    st.session_state.edit_mode[edit_key] = False
                    st.rerun()
            else:
                cols[1].markdown(habit.name)

                if cols[2].button("Edit", key=f"{priority}_edit_{i}"):
                    st.session_state.edit_mode[edit_key] = True
                    st.rerun()

            if cols[3].button("Delete", key=f"{priority}_delete_{i}"):
                habits.remove(habit)
                save_habits(habits)
                st.rerun()

    new_habit_name = st.text_input("Add a new habit")
    priority = st.selectbox(
        "Select priority", ["red", "orange", "green"], index=2)

    if st.button("Add Habit") and new_habit_name.strip():
        new_habit = Habit(new_habit_name, priority=priority)
        habits.append(new_habit)
        save_habits(habits)
        st.rerun()


if __name__ == "__main__":
    main()
