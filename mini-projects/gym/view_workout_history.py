import streamlit as st
import json

# --- Page Setup ---
st.set_page_config(page_title="📖 Workout History", layout="centered")
st.title("📖 Past Workout History")

# --- Load Data ---
def load_workouts(filename="gym_workouts.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []

# --- Display Workouts ---
workouts = load_workouts()

if not workouts:
    st.warning("No saved workouts found. Go add some first!")
else:
    for i, workout in enumerate(reversed(workouts)):  # Show most recent first
        with st.expander(f"🗓️ {workout['date']}"):
            for ex in workout["exercises"]:
                if ex["type"] == "Strength":
                    st.write(f"🏋️ {ex['name']}: {ex['sets']} x {ex['reps']} @ {ex['weight']}kg")
                elif ex["type"] == "Cardio":
                    st.write(f"🏃 {ex['name']}: {ex['duration']} mins, {ex['distance']} km")
                else:
                    st.write(f"📌 {ex['name']} (type: {ex['type']})")