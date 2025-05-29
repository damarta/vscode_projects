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


def display_habits(habits, goals):
    priority_colors = {"red": "🔴", "orange": "🟠", "green": "🟢"}
    for i, habit in enumerate(habits):
        done = st.checkbox(f"{priority_colors.get(habit.priority, '⚪')} {habit.name}",
                           value=habit.done, key=f"habit_{habit.name}_{i}")
        if done != habit.done:
            habit.done = done
            save_goals(goals)
            st.rerun()


def display_daily_goals(daily_goals, goals):
    for day in daily_goals:
        with st.expander(f"Day: {day.date}"):
            display_habits(day.habits, goals)


def display_weekly_goals(weekly_goals, goals):
    for week in weekly_goals:
        with st.expander(f"Week {week.week_number}"):
            display_daily_goals(week.daily_goals, goals)


def display_monthly_goals(monthly_goals):
    for month in monthly_goals:
        with st.expander(f"Month: {month.month}/{month.year}"):
            display_weekly_goals(month.weekly_goals, monthly_goals)


def main():
    st.title("Habit Tracker with Goal Hierarchy")

    goals = load_goals()

    if not goals:
        st.info("No goals found. Please add goals in the JSON file.")

    display_monthly_goals(goals)


if __name__ == "__main__":
    main()
