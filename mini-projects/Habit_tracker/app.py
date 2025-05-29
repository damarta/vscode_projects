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

    with st.sidebar:
        st.header("Filter Habits")

        status_filter = st.selectbox(
            "Status", ["All", "Done", "Not Done"], index=0)
        priority_filter = st.selectbox(
            "Priority", ["All", "Red", "Orange", "Green"], index=0)
        sort_option = st.selectbox("Sort by", ["Priority", "Name"], index=0)

    # Filter by status
    if status_filter == "Done":
        habits = [h for h in habits if h.done]
    elif status_filter == "Not Done":
        habits = [h for h in habits if not h.done]

    # Filter by priority
    if priority_filter != "All":
        habits = [h for h in habits if h.priority == priority_filter.lower()]

    # Sorting
    if sort_option == "Name":
        habits.sort(key=lambda h: h.name)
    else:  # Priority sorting
        priority_order = {"red": 0, "orange": 1, "green": 2}
        habits.sort(key=lambda h: priority_order[h.priority])

    st.header("Your Habits")

    priority_colors = {"red": "🔴", "orange": "🟠", "green": "🟢"}

    for i, habit in enumerate(habits):
        cols = st.columns([0.05, 0.7, 0.1, 0.1])
        done = cols[0].checkbox("", value=habit.done, key=f"done_{i}")
        if done != habit.done:
            habit.done = done
            save_habits(habits)
            st.rerun()

        # Display priority emoji next to habit name
        display_name = f"{priority_colors[habit.priority]} {habit.name}"

        # Initialize edit_mode dict if not exists
        if 'edit_mode' not in st.session_state:
            st.session_state.edit_mode = {}

        edit_key = f"habit_{i}"

        if st.session_state.edit_mode.get(edit_key, False):
            new_name = cols[1].text_input("Edit Habit Name", value=habit.name,
                                          key=f"name_input_{i}")
            if cols[2].button("Save", key=f"save_{i}"):
                if new_name.strip():
                    habit.name = new_name.strip().title()
                    save_habits(habits)
                    st.session_state.edit_mode[edit_key] = False
                    st.rerun()
            if cols[3].button("Cancel", key=f"cancel_{i}"):
                st.session_state.edit_mode[edit_key] = False
                st.rerun()
        else:
            cols[1].markdown(display_name)

            if cols[2].button("Edit", key=f"edit_{i}"):
                st.session_state.edit_mode[edit_key] = True
                st.rerun()

        if cols[3].button("Delete", key=f"delete_{i}"):
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
