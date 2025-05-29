import streamlit as st
import json
import os
from goals import MonthlyGoal  # Make sure this file is in the same folder

DATA_FILE = "habits.json"  # Adjust if you named it differently


def load_goals():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [MonthlyGoal.from_dict(m) for m in data]
    return []


def save_goals(goals):
    with open(DATA_FILE, "w") as f:
        json.dump([g.to_dict() for g in goals], f, indent=2)


def flatten_habits(goals):
    all_habits = []
    for month in goals:
        for week in month.weekly_goals:
            for day in week.daily_goals:
                all_habits.extend(day.habits)
    return all_habits


def display_habits(habits, goals):
    priority_colors = {"red": "🔴", "orange": "🟠", "green": "🟢"}

    # Initialize edit_mode dict if not exists
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = {}

    for i, habit in enumerate(habits):
        cols = st.columns([0.05, 0.7, 0.1, 0.1])
        done = cols[0].checkbox("", value=habit.done, key=f"done_{i}")
        if done != habit.done:
            habit.done = done
            save_goals(goals)
            st.rerun()

        # Display priority emoji next to habit name
        display_name = f"{priority_colors.get(habit.priority, '⚪')} {habit.name}"

        edit_key = f"habit_{i}"

        if st.session_state.edit_mode.get(edit_key, False):
            new_name = cols[1].text_input("Edit Habit Name", value=habit.name,
                                          key=f"name_input_{i}")
            if cols[2].button("Save", key=f"save_{i}"):
                if new_name.strip():
                    habit.name = new_name.strip().title()
                    save_goals(goals)
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
            save_goals(goals)
            st.rerun()


def main():
    st.title("📋 Habit Tracker")
    st.caption("Track your daily progress below.")
    st.markdown("---")

    st.header("📅 Daily Goals")

    goals = load_goals()

    if not goals:
        st.info("No goals found. Please add goals in the JSON file.")

    # Sidebar filters and sorting
    with st.sidebar:
        st.header("Filter Habits")

        status_filter = st.selectbox(
            "Status", ["All", "Done", "Not Done"], index=0)
        priority_filter = st.selectbox(
            "Priority", ["All", "Red", "Orange", "Green"], index=0)
        sort_option = st.selectbox("Sort by", ["Priority", "Name"], index=0)

    all_habits = flatten_habits(goals)

    # Apply filters
    if status_filter == "Done":
        filtered = [h for h in all_habits if h.done]
    elif status_filter == "Not Done":
        filtered = [h for h in all_habits if not h.done]
    else:
        filtered = all_habits

    if priority_filter != "All":
        filtered = [h for h in filtered if h.priority ==
                    priority_filter.lower()]

    # Apply sorting
    if sort_option == "Name":
        filtered.sort(key=lambda h: h.name)
    else:
        priority_order = {"red": 0, "orange": 1, "green": 2}
        filtered.sort(key=lambda h: priority_order.get(h.priority, 3))

    display_habits(filtered, goals)

    # Temporary: export clean JSON file for readability testing
    with open("demo_export.json", "w") as f:
        json.dump([h.to_dict() for h in all_habits], f, indent=2)


if __name__ == "__main__":
    main()
