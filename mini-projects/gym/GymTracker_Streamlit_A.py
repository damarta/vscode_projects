import streamlit as st
import json 
from datetime import datetime

# ---  Core logic ---

def save_to_json(entry, filename="gym_workouts.json"):

    try:
        with open(filename, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# --- UI Section ---

st.title("🏋️ Gym Tracker App -- Simple Entry")

exercise_type = st.selectbox("Choose exercise type", ["Strength", "Cardio"])
name = st.text_input("Exercise name")

if exercise_type == "Strength":

    sets = st.number_input("Sets", min_value=1, max_value=20, step=1)
    reps = st.number_input("Reps", min_value=1, max_value=50, step=1)
    weight = st.number_input("weight (kg)", min_value=0.0, step=2.5)

elif exercise_type == "Cardio":
    duration = st.number_input("Duration (mins)", min_value=1, step=1)
    distance = st.number_input("Distance (km)", min_value=0.1, step=0.1)

if st.button("💾 Save Workout"):
    entry = {
        "type": exercise_type,
        "name": name,
        "date": datetime.now().strftime("%Y-%m-%d %H-%m-%S"),
    }

    if exercise_type == "Strength":
        entry["sets"] = sets
        entry["reps"] = reps
        entry["weight"] = weight
    else:
        entry["duration"] = duration
        entry["distance"] = distance

    #save
    save_to_json(entry)
    st.success("✅ Workout saved!")