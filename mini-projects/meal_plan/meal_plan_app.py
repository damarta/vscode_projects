import streamlit as st
import random

# Meals with dietary tags
breakfast_options = [
    ("Protein shake", "High Protein"),
    ("Protein Carrey Cake", "Vegetarian"),
    ("Pizza", "None")
]

lunch_options = [
    ("Protein shake", "High Protein"),
    ("Protein Carrey Cake", "Vegetarian"),
    ("Chicken Rap", "High Protein"),
    ("Chicken Burrito meal", "None")
]

dinner_options = [
    ("Pizza", "None"),
    ("Protein Carrey Cake", "Vegetarian"),
    ("Chicken Rap", "High Protein"),
    ("Chicken Burrito meal", "None")
]

# Function to filter meals
def filter_meals(options_list, tag):
    if tag == "None":
        return options_list
    return [meal for meal in options_list if meal[1].lower() == tag.lower()]

# Streamlit UI
st.title("🍽️ Meal Plan Generator")

# Dropdown for diet type
diet_filter = st.selectbox("Choose your dietary preference:", ["None", "High Protein", "Vegetarian"])

# Button to generate plan
if st.button("Generate Meal Plan"):
    bf = random.choice(filter_meals(breakfast_options, diet_filter))
    ln = random.choice(filter_meals(lunch_options, diet_filter))
    dn = random.choice(filter_meals(dinner_options, diet_filter))

    st.subheader("Your Meal Plan:")
    st.markdown(f"🥣 **Breakfast**: {bf[0]} ({bf[1]})")
    st.markdown(f"🥪 **Lunch**: {ln[0]} ({ln[1]})")
    st.markdown(f"🍛 **Dinner**: {dn[0]} ({dn[1]})")
