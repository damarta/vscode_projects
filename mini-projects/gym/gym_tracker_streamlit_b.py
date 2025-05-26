import streamlit as st
import json
from datetime import datetime

# ---------------- Storage ----------------

def save_workout_to_json(workout, filename="gym_workouts.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(workout)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# ---------------- App UI ----------------

st.title("🏋️ GymTracker – Full Workout Logger")

# Session state to store all exercises
if "exercises" not in st.session_state:
    st.session_state.exercises = []

st.subheader("➕ Add Exercise")

exercise_type = st.selectbox("Type", ["Strength", "Cardio"], key="type")
name = st.text_input("Exercise name", key="name")

if exercise_type == "Strength":
    sets = st.number_input("Sets", min_value=1, max_value=20, step=1)
    reps = st.number_input("Reps", min_value=1, max_value=50, step=1)
    weight = st.number_input("Weight (kg)", min_value=0.0, step=2.5)

elif exercise_type == "Cardio":
    duration = st.number_input("Duration (min)", min_value=1, step=1)
    distance = st.number_input("Distance (km)", min_value=0.1, step=0.1)

# Add button to store exercise in memory
if st.button("➕ Add to Workout"):
    if not name:
        st.warning("⚠️ Please enter an exercise name.")
    else:
        entry = {
            "type": exercise_type,
            "name": name
        }

        if exercise_type == "Strength":
            entry.update({
                "sets": sets,
                "reps": reps,
                "weight": weight
            })
        else:
            entry.update({
                "duration": duration,
                "distance": distance
            })

        st.session_state.exercises.append(entry)
        st.success(f"✅ Added: {name}")

# Show current workout
if st.session_state.exercises:
    st.subheader("📋 Current Workout")
    for i, ex in enumerate(st.session_state.exercises):
        if ex["type"] == "Strength":
            st.write(f"{i+1}. {ex['name']} — {ex['sets']}x{ex['reps']} @ {ex['weight']}kg")
        else:
            st.write(f"{i+1}. {ex['name']} — {ex['duration']}min, {ex['distance']}km")

    if st.button("💾 Save Workout Session"):
        full_workout = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exercises": st.session_state.exercises
        }
        save_workout_to_json(full_workout)
        st.success("💪 Workout session saved!")
        st.session_state.exercises = []

else:
    st.info("No exercises added yet.")