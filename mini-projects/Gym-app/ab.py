import random
import streamlit as st

# Title
st.title("🚀 Build Your Body. Fuel Your Life.")

st.caption(
    "The ultimate personalized training & nutrition system — built just for you.")

# CTA Button after subtitle
st.markdown("### 💥 Ready to Transform?")
if st.button("🚀 Start Your Plan Now"):
    st.rerun()

# Section 1: Sport Selection
st.header("1. 🏆 Choose Your Training Style")
st.markdown("""
Not all workouts are created equal. Your sport drives your training intensity — and your fuel strategy.
""")
sport = st.multiselect("🏋️ Select your training types:", [
    "🏋️ Bodybuilding",
    "🏃 Running",
    "🔥 CrossFit",
    "💪 Full Body",
    "🫀 Conditioning",
    "🥋 BJJ",
    "🥊 Kickboxing",
    "🥊 Boxing",
    "🚴 Cycling",
    "🏊 Swimming",
    "🧘 Pilates",
    "🧘‍♂️ Yoga",
    "💃 Dance (Zumba, Hip-Hop, Salsa)",
    "🧠 Meditation & Breathwork"
])


st.caption(
    "💡 Tip: Select all sports you regularly train. We'll calculate your average macro needs.")

# 🎯 Motivational Quotes based on selected sports
if sport:
    st.markdown("### 🧠 Personalized Motivation")

    sport_quotes = {
        "🧠 Meditation & Breathwork": "🧘‍♀️ Calm mind. Strong body. Powerful life.",
        "🧘‍♂️ Yoga": "🧘‍♂️ Balance is not something you find. It's something you create.",
        "🧘 Pilates": "🔄 Flexibility is strength in disguise.",
        "💃 Dance (Zumba, Hip-Hop, Salsa)": "💃 Feel the rhythm, fuel your energy.",
        "🥋 BJJ": "🥋 Patience, pressure, power. You’re training like a warrior.",
        "🥊 Kickboxing": "🥊 Strike with purpose. Fuel with intention.",
        "🥊 Boxing": "🥊 Discipline forged in sweat. You're a fighter inside and out.",
        "🔥 CrossFit": "🔥 Push your limits. Then break them.",
        "🏃 Running": "🏃‍♂️ One step at a time, you're going the distance."
    }

    # Display relevant quotes for selected sports
    displayed = set()
    for s in sport:
        quote = sport_quotes.get(s)
        if quote and quote not in displayed:
            st.info(quote)
            displayed.add(quote)

# Section 2: User Details
st.header("2. Enter Your Details")

age = st.number_input("Age", min_value=10, max_value=100, value=25)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Fitness Goal Section: Improved copy and formatting
st.subheader("🎯 Your Goal")
st.markdown("What are you working toward right now?")

goal = st.radio("Choose your current objective:", [
    "🔥 Lose Fat – Trim down and lean out",
    "💪 Build Muscle – Bulk up with clean mass",
    "⚖️ Maintain – Stay balanced and consistent"
])

# 🔥 Activity Level
st.subheader("🔥 Your Activity Level")

st.markdown("""
To tailor your diet, we need to know how much you burn.  
Use your smartwatch, Fitbit, or just your common sense.  
Choose the option that reflects your average **daily burn**:
""")

activity_level = st.radio("", [
    "🛋️ Low – Sedentary (under 2,000 kcal/day)",
    "🚶 Moderate – Some activity (2,000–2,500 kcal/day)",
    "🏃 High – Active lifestyle (2,500+ kcal/day)"
])

st.caption("""💡 Why this matters: Your calorie needs change dramatically based on activity.
More burn = more food (yes, really).""")

# Section 2.5: Diet Preference
st.subheader("Preferred Diet Type")

diet_type = st.selectbox("Choose your diet style:", [
    "Standard (Mixed Meals)",
    "Vegetarian (No meat, may include dairy/eggs)",
    "Vegan (No animal products)",
    "Keto (Low carb, high fat)",
    "Pescatarian (Fish allowed, no red meat)",
    "High Protein Focus"
])

# Summary Recap
st.markdown("---")
st.markdown("### 👤 Your Setup Summary")

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"**🧓 Age**: {age} years")
    st.markdown(f"**⚖️ Weight**: {weight} kg")
    st.markdown(f"**🥗 Diet Preference**: {diet_type}")

with col2:
    st.markdown(f"**🎯 Goal**: {goal}")
    st.markdown(f"**🔥 Activity Level**: {activity_level}")
    if sport:
        st.markdown(f"**🏋️ Training Types**: {', '.join(sport)}")

# Section 3: Macronutrient Calculator
st.header("3. Your Macronutrients")
if st.button("Calculate Macros"):
    # Define sport-specific multipliers
    macro_profiles = {
        "🏋️ Bodybuilding":     {"cal": 32, "pro": 2.2, "fat": 1.0},
        "🏃 Running":          {"cal": 28, "pro": 1.6, "fat": 0.8},
        "🔥 CrossFit":         {"cal": 34, "pro": 2.0, "fat": 0.9},
        "💪 Full Body":        {"cal": 30, "pro": 1.8, "fat": 0.8},
        "🫀 Conditioning":     {"cal": 29, "pro": 1.7, "fat": 0.7},
        "🥋 BJJ":              {"cal": 33, "pro": 2.0, "fat": 0.85},
        "🥊 Kickboxing":       {"cal": 33, "pro": 2.0, "fat": 0.85},
        "🥊 Boxing":           {"cal": 32, "pro": 2.0, "fat": 0.8},
        "🚴 Cycling":          {"cal": 27, "pro": 1.5, "fat": 0.75},
        "🏊 Swimming":         {"cal": 30, "pro": 1.7, "fat": 0.8},
        "🧘 Pilates":           {"cal": 26, "pro": 1.4, "fat": 0.7},
        "🧘‍♂️ Yoga":              {"cal": 25, "pro": 1.2, "fat": 0.6},
        "💃 Dance (Zumba, Hip-Hop, Salsa)": {"cal": 29, "pro": 1.5, "fat": 0.75},
        "🧠 Meditation & Breathwork":      {"cal": 22, "pro": 1.1, "fat": 0.5}
    }

    # Aggregate selected profiles
    if sport:
        avg_cal = sum(macro_profiles[s]["cal"] for s in sport) / len(sport)
        avg_pro = sum(macro_profiles[s]["pro"] for s in sport) / len(sport)
        avg_fat = sum(macro_profiles[s]["fat"] for s in sport) / len(sport)

        calories = weight * avg_cal
        protein = weight * avg_pro
        fats = weight * avg_fat
        carbs = (calories - (protein * 4 + fats * 9)) / 4

        st.success("Daily Intake Goals")
        st.write(f"Calories: {calories:.0f} kcal")
        st.write(f"Protein: {protein:.0f} g")
        st.write(f"Fats: {fats:.0f} g")
        st.write(f"Carbs: {carbs:.0f} g")
    else:
        st.warning(
            "Please select at least one training style to calculate your macros.")

# Section 4: Meal Plan Generator

# Define simple meal database (macros in g)
meal_db = {
    "Standard (Mixed Meals)": {
        "Breakfast": [
            {"name": "Oats with milk and banana",
                "protein": 20, "carbs": 45, "fat": 10},
            {"name": "Scrambled eggs with spinach and toast",
                "protein": 22, "carbs": 30, "fat": 15}
        ],
        "Lunch": [
            {"name": "Grilled chicken, quinoa, veggies",
                "protein": 40, "carbs": 50, "fat": 18},
            {"name": "Beef stir-fry with rice",
                "protein": 35, "carbs": 60, "fat": 20}
        ],
        "Dinner": [
            {"name": "Salmon with sweet potato",
                "protein": 38, "carbs": 40, "fat": 22},
            {"name": "Turkey meatballs with pasta",
                "protein": 36, "carbs": 55, "fat": 17}
        ],
        "Snack": [
            {"name": "Greek yogurt with almonds",
                "protein": 18, "carbs": 10, "fat": 12},
            {"name": "Protein shake with peanut butter",
                "protein": 25, "carbs": 5, "fat": 15}
        ]
    },
    "Vegetarian (No meat, may include dairy/eggs)": {
        "Breakfast": [
            {"name": "Tofu scramble with veggies",
                "protein": 20, "carbs": 15, "fat": 12},
            {"name": "Oats with almond milk and nuts",
                "protein": 18, "carbs": 35, "fat": 14}
        ],
        "Lunch": [
            {"name": "Chickpea salad with olive oil",
                "protein": 25, "carbs": 45, "fat": 20},
            {"name": "Lentil soup and wholegrain bread",
                "protein": 22, "carbs": 50, "fat": 10}
        ],
        "Dinner": [
            {"name": "Paneer curry with rice",
                "protein": 28, "carbs": 55, "fat": 25},
            {"name": "Stuffed bell peppers with quinoa",
                "protein": 26, "carbs": 40, "fat": 18}
        ],
        "Snack": [
            {"name": "Hummus and carrots", "protein": 10, "carbs": 15, "fat": 8},
            {"name": "Cottage cheese with berries",
                "protein": 15, "carbs": 12, "fat": 5}
        ]
    }
}

#
# Section 4: Meal Plan Generator
st.header("4. 🍽️ Your Personalized Meal Plan")
st.markdown(
    "Built from your goals. Matched to your movement. Balanced to your macros.")

if st.button("Generate Meal Plan"):
    st.subheader("Your Daily Meal Plan")
    st.markdown(
        "This meal plan is designed for **your body**, **your sport**, and **your macros**.")
    st.markdown(f"**Diet Preference:** {diet_type}")

    if diet_type not in meal_db:
        st.warning("""This diet style is not yet supported in the meal database.
        Please choose 'Standard' or 'Vegetarian' for now.""")
    else:
        selected_meals = {}
        totals = {"protein": 0, "carbs": 0, "fat": 0}

        for meal_time in ["Breakfast", "Lunch", "Dinner", "Snack"]:
            meal = random.choice(meal_db[diet_type][meal_time])
            selected_meals[meal_time] = meal
            totals["protein"] += meal["protein"]
            totals["carbs"] += meal["carbs"]
            totals["fat"] += meal["fat"]

        for meal_time, meal in selected_meals.items():
            st.markdown(f"### 🍽️ {meal_time}")
            st.write(f"• {meal['name']}")
            st.caption(
                f"Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g")

        # Calculate daily calories from macros
        total_calories = totals["protein"] * 4 + \
            totals["carbs"] * 4 + totals["fat"] * 9

        st.markdown("---")
        st.markdown("### 🧮 Daily Totals vs Your Targets")

        st.write(f"**Target Calories:** {calories:.0f} kcal")
        st.write(f"**Target Protein:** {protein:.0f}g")
        st.write(f"**Target Carbs:** {carbs:.0f}g")
        st.write(f"**Target Fats:** {fats:.0f}g")

        st.markdown("**Total from Plan:**")
        st.write(f"Calories: {total_calories:.0f} kcal")
        st.write(f"Protein: {totals['protein']}g")
        st.write(f"Carbs: {totals['carbs']}g")
        st.write(f"Fats: {totals['fat']}g")

        st.info("Want different meals? Just re-run the plan to swap randomly!")
        st.success(
            "Meal plan generated based on your diet preference and macro goals!")
        st.markdown(
            "#### 🔁 Not feeling a meal? Just press 'Generate Meal Plan' again to discover a new set. It's like meal inspiration on demand.")

# Section 5: Grocery List Generator
st.header("5. 🛒 Your Smart Grocery List (Coming Soon)")
st.markdown(
    "Get a done-for-you shopping list from your custom meals. 🧺 No guesswork. Just great food.")
st.caption("📦 Fuel your goals without overbuying or wasting time.")
