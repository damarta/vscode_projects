# main.py — Gym Planner App Framework

import streamlit as st
from datetime import datetime

# -------- App Config --------
st.set_page_config(page_title="🏋🏾‍♂️Gym Planner App🏋🏾‍♂️", layout="wide")


# -------- Sidebar Navigation --------
st.sidebar.title("🏋️ Gym Planner Menu")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "👤 Personal Info",
    "🔥 Macro Calculator",
    "🍽️ Meal Plan Generator",
    "🛒 Grocery List",
    "📤 Export & Save"
])

st.markdown("# Gym Planner App")
st.markdown(
    "Your all-in-one tool for fitness nutrition, training, and tracking 💪")


# -------- Initialize session_state --------
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "macro_data" not in st.session_state:
    st.session_state.macro_data = {}

if "meal_plan" not in st.session_state:
    st.session_state.meal_plan = []

if "grocery_list" not in st.session_state:
    st.session_state.grocery_list = []

# -------- Pages --------

if page == "🏠 Home":
    st.subheader("Welcome to your Gym Planner 💡")
    st.markdown("""
    Use the sidebar to navigate through:
    - Input personal fitness goals
    - Calculate your ideal macros
    - Generate daily meal plans
    - Build a grocery list
    - Export everything as JSON or PDF
    """)

elif page == "👤 Personal Info":
    st.subheader("Step 1: Personal Information")

    with st.form("user_info_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=10, max_value=100, step=1)
            gender = st.radio("Gender", ["Male", "Female", "Other"])
            height = st.number_input(
                "Height (cm)", min_value=120, max_value=250, step=1)

        with col2:
            weight = st.number_input(
                "Current Weight (kg)", min_value=30.0, max_value=200.0, step=0.5)
            goal = st.selectbox(
                "Goal", ["Lose Weight", "Maintain", "Gain Muscle"])
            activity = st.selectbox("Activity Level", [
                "Sedentary",
                "Lightly Active",
                "Moderately Active",
                "Very Active",
                "Athlete"
            ])

        diet_type = st.selectbox(
            "Preferred Diet", ["None", "High Protein", "Vegetarian", "Keto", "Vegan"])
        sport = st.selectbox("Main Sport", [
                             "Gym", "CrossFit", "Running", "BJJ", "Cycling", "Bodybuilding", "Other"])

        submitted = st.form_submit_button("💾 Save Info")

    if submitted:
        st.session_state.user_data = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "goal": goal,
            "activity": activity,
            "diet_type": diet_type,
            "sport": sport
        }
        st.success("✅ Personal info saved!")

        st.json(st.session_state.user_data)

elif page == "🔥 Macro Calculator":
    st.subheader("Step 2: Macro Calculator")
    st.write("📊 Coming next: calories, protein, carbs, fats logic.")

elif page == "🍽️ Meal Plan Generator":
    st.subheader("Step 3: Meal Planner")
    st.write("🥗 Coming next: auto-generate based on macros & diet type.")

elif page == "🛒 Grocery List":
    st.subheader("Step 4: Grocery List")
    st.write("🛒 Coming next: convert meal plan into grocery checklist.")

elif page == "📤 Export & Save":
    st.subheader("Final Step: Export Data")
    st.write("💾 Coming next: JSON / PDF / download options.")
