import streamlit as st

# Initialize wizard step and started flag
if "step" not in st.session_state:
    st.session_state.step = 1
if "started" not in st.session_state:
    st.session_state.started = False

def next_step():
    st.session_state.step += 1

def start_app():
    st.session_state.started = True
    st.session_state.step = 1

# Welcome screen and step label/progress bar
if not st.session_state.started:
    st.title("🏋️ Welcome to the Gym Planner App")
    st.markdown("Create your personalized workout and nutrition strategy in just a few steps.")
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921822.png", width=120)
    st.button("🚀 Start My Plan", on_click=start_app)
else:
    st.title("🚀 Build Your Body. Fuel Your Life.")
    st.caption("The ultimate personalized training & nutrition system — built just for you.")
    step_labels = {
        1: "Step 1: Training Style",
        2: "Step 2: Personal Info",
        3: "Step 3: Diet Preference",
        4: "Step 4: Macro Plan",
        5: "Step 5: Meal Plan",
        6: "Step 6: Grocery List"
    }
    st.markdown(f"#### ✅ {step_labels[st.session_state.step]}")
    st.progress((st.session_state.step - 1) / 5)


# Only show steps if started
if st.session_state.started:
    # Step 1: Training Style
    if st.session_state.step == 1:
        st.markdown("### Step 1: What kind of training do you do?")
        sport = st.multiselect("🏋️ Select your training types:", [
            "🏋️ Bodybuilding", "🏃 Running", "🔥 CrossFit", "💪 Full Body", "🫀 Conditioning",
            "🥋 BJJ", "🥊 Kickboxing", "🥊 Boxing", "🚴 Cycling", "🏊 Swimming",
            "🧘 Pilates", "🧘‍♂️ Yoga", "💃 Dance (Zumba, Hip-Hop, Salsa)", "🧠 Meditation & Breathwork"
        ])
        # Save to session_state
        st.session_state.sport = sport
        if sport:
            st.button("Next ➡️", on_click=next_step)

    # Step 2: Personal Info (with input validation and Back button)
    if st.session_state.step == 2:
        st.markdown("### Step 2: Tell us about yourself")
        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=st.session_state.get('age', 25)
        )
        weight = st.number_input(
            "Weight (kg)",
            min_value=30,
            max_value=200,
            value=st.session_state.get('weight', 70)
        )
        goal = st.radio(
            "Your Goal",
            ["🔥 Lose Fat", "💪 Build Muscle", "⚖️ Maintain"],
            index=["🔥 Lose Fat", "💪 Build Muscle", "⚖️ Maintain"].index(st.session_state.get('goal', "🔥 Lose Fat"))
        )
        activity_level = st.radio(
            "Your Activity Level",
            [
                "🛋️ Low – Sedentary",
                "🚶 Moderate – Some activity",
                "🏃 High – Active lifestyle"
            ],
            index=[
                "🛋️ Low – Sedentary",
                "🚶 Moderate – Some activity",
                "🏃 High – Active lifestyle"
            ].index(st.session_state.get('activity_level', "🛋️ Low – Sedentary"))
        )

        # Save inputs
        st.session_state.age = age
        st.session_state.weight = weight
        st.session_state.goal = goal
        st.session_state.activity_level = activity_level

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Back"):
                st.session_state.step = 1
        with col2:
            if age and weight and goal and activity_level:
                if st.button("Next ➡️"):
                    st.session_state.step = 3
            else:
                st.warning("Please fill in all fields to proceed.")

    # Step 3: Diet Style (with input validation and Back button)
    if st.session_state.step == 3:
        st.markdown("### Step 3: Pick your preferred diet")
        diet_type = st.selectbox(
            "Diet Preference",
            [
                "Standard (Mixed Meals)", "Vegetarian", "Vegan", "Keto", "Pescatarian", "High Protein Focus"
            ],
            index=[
                "Standard (Mixed Meals)", "Vegetarian", "Vegan", "Keto", "Pescatarian", "High Protein Focus"
            ].index(st.session_state.get('diet_type', "Standard (Mixed Meals)"))
        )

        st.session_state.diet_type = diet_type

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Back"):
                st.session_state.step = 2
        with col2:
            if diet_type:
                if st.button("Next ➡️"):
                    st.session_state.step = 4
            else:
                st.warning("Please select a diet preference to proceed.")

    # Step 4: Recap & Macros
    if st.session_state.step == 4:
        st.markdown("### Step 4: Your Macro Plan")

        # Macro calculation
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

        # Calculate averages
        if sport:
            avg_cal = sum(macro_profiles[s]["cal"] for s in sport) / len(sport)
            avg_pro = sum(macro_profiles[s]["pro"] for s in sport) / len(sport)
            avg_fat = sum(macro_profiles[s]["fat"] for s in sport) / len(sport)

            calories = weight * avg_cal
            protein = weight * avg_pro
            fats = weight * avg_fat
            carbs = (calories - (protein * 4 + fats * 9)) / 4

            st.success("Here’s your daily fuel plan 💪")
            st.write(f"Calories: {calories:.0f} kcal")
            st.write(f"Protein: {protein:.0f} g")
            st.write(f"Fats: {fats:.0f} g")
            st.write(f"Carbs: {carbs:.0f} g")

            if st.button("Next ➡️"):
                next_step()
        else:
            st.warning("Please select at least one training type in Step 1.")

    # Step 5: Meal Plan (dynamic generation)
    if st.session_state.step == 5:
        st.markdown("### Step 5: Your Meal Plan")

        meal_db = {
            "Standard (Mixed Meals)": {
                "Breakfast": [
                    {"name": "Oats with milk and banana", "protein": 20, "carbs": 45, "fat": 10},
                    {"name": "Scrambled eggs with spinach and toast", "protein": 22, "carbs": 30, "fat": 15}
                ],
                "Lunch": [
                    {"name": "Grilled chicken, quinoa, veggies", "protein": 40, "carbs": 50, "fat": 18},
                    {"name": "Beef stir-fry with rice", "protein": 35, "carbs": 60, "fat": 20}
                ],
                "Dinner": [
                    {"name": "Salmon with sweet potato", "protein": 38, "carbs": 40, "fat": 22},
                    {"name": "Turkey meatballs with pasta", "protein": 36, "carbs": 55, "fat": 17}
                ],
                "Snack": [
                    {"name": "Greek yogurt with almonds", "protein": 18, "carbs": 10, "fat": 12},
                    {"name": "Protein shake with peanut butter", "protein": 25, "carbs": 5, "fat": 15}
                ]
            },
            "Vegetarian": {
                "Breakfast": [
                    {"name": "Tofu scramble with veggies", "protein": 20, "carbs": 15, "fat": 12},
                    {"name": "Oats with almond milk and nuts", "protein": 18, "carbs": 35, "fat": 14}
                ],
                "Lunch": [
                    {"name": "Chickpea salad with olive oil", "protein": 25, "carbs": 45, "fat": 20},
                    {"name": "Lentil soup and wholegrain bread", "protein": 22, "carbs": 50, "fat": 10}
                ],
                "Dinner": [
                    {"name": "Paneer curry with rice", "protein": 28, "carbs": 55, "fat": 25},
                    {"name": "Stuffed bell peppers with quinoa", "protein": 26, "carbs": 40, "fat": 18}
                ],
                "Snack": [
                    {"name": "Hummus and carrots", "protein": 10, "carbs": 15, "fat": 8},
                    {"name": "Cottage cheese with berries", "protein": 15, "carbs": 12, "fat": 5}
                ]
            }
        }

        import random

        diet_key = diet_type if 'diet_type' in locals() and diet_type in meal_db else "Standard (Mixed Meals)"

        if 'calories' in locals() and 'protein' in locals() and 'fats' in locals() and 'carbs' in locals():
            calories = calories
            protein = protein
            fats = fats
            carbs = carbs
        else:
            calories = 2200
            protein = 140
            fats = 70
            carbs = 250

        if calories and protein and fats and carbs:
            st.write("Here is a meal plan tailored to your macros:")

            selected_meals = {}
            totals = {"protein": 0, "carbs": 0, "fat": 0}

            for meal_time in ["Breakfast", "Lunch", "Dinner", "Snack"]:
                meal = random.choice(meal_db[diet_key][meal_time])
                selected_meals[meal_time] = meal
                totals["protein"] += meal["protein"]
                totals["carbs"] += meal["carbs"]
                totals["fat"] += meal["fat"]

            # Save selected meals to session state for grocery list step
            st.session_state.selected_meals = selected_meals

            for meal_time, meal in selected_meals.items():
                st.markdown(f"#### {meal_time}")
                st.write(f"• {meal['name']}")
                st.caption(f"Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g")

            total_calories = totals["protein"] * 4 + totals["carbs"] * 4 + totals["fat"] * 9
            st.markdown("---")
            st.markdown("### Daily Totals")
            st.write(f"Calories: {total_calories:.0f} kcal")
            st.write(f"Protein: {totals['protein']}g")
            st.write(f"Carbs: {totals['carbs']}g")
            st.write(f"Fats: {totals['fat']}g")

            if st.button("Generate New Meal Plan"):
                st.experimental_rerun()
        else:
            st.warning("Please calculate your macros first in Step 4.")

    # Step 6: Grocery List
    if st.session_state.step == 6:
        st.markdown("### Step 6: Your Grocery List")

        ingredient_db = {
            "Oats with milk and banana": {
                "Oats": "50g",
                "Milk": "200ml",
                "Banana": "1 medium"
            },
            "Scrambled eggs with spinach and toast": {
                "Eggs": "3",
                "Spinach": "50g",
                "Wholegrain toast": "2 slices"
            },
            "Grilled chicken, quinoa, veggies": {
                "Chicken breast": "150g",
                "Quinoa": "100g",
                "Mixed vegetables": "150g",
                "Olive oil": "1 tbsp"
            },
            "Beef stir-fry with rice": {
                "Beef strips": "150g",
                "Rice": "100g",
                "Mixed vegetables": "150g",
                "Soy sauce": "1 tbsp"
            },
            "Salmon with sweet potato": {
                "Salmon fillet": "150g",
                "Sweet potato": "200g",
                "Broccoli": "100g"
            },
            "Turkey meatballs with pasta": {
                "Turkey meatballs": "150g",
                "Pasta": "100g",
                "Tomato sauce": "50g"
            },
            "Greek yogurt with almonds": {
                "Greek yogurt": "150g",
                "Almonds": "30g"
            },
            "Protein shake with peanut butter": {
                "Protein powder": "1 scoop",
                "Peanut butter": "1 tbsp",
                "Milk": "200ml"
            },
            "Tofu scramble with veggies": {
                "Tofu": "150g",
                "Mixed veggies": "100g",
                "Olive oil": "1 tbsp"
            },
            "Oats with almond milk and nuts": {
                "Oats": "50g",
                "Almond milk": "200ml",
                "Mixed nuts": "30g"
            },
            "Chickpea salad with olive oil": {
                "Chickpeas": "150g",
                "Olive oil": "1 tbsp",
                "Salad veggies": "100g"
            },
            "Lentil soup and wholegrain bread": {
                "Lentils": "150g",
                "Wholegrain bread": "2 slices"
            },
            "Paneer curry with rice": {
                "Paneer": "150g",
                "Rice": "100g",
                "Curry sauce": "100g"
            },
            "Stuffed bell peppers with quinoa": {
                "Bell peppers": "2",
                "Quinoa": "100g",
                "Mixed veggies": "100g"
            },
            "Hummus and carrots": {
                "Hummus": "100g",
                "Carrots": "100g"
            },
            "Cottage cheese with berries": {
                "Cottage cheese": "150g",
                "Berries": "100g"
            }
        }

        selected_meals = st.session_state.get("selected_meals", None)

        if selected_meals is None:
            st.warning("Please generate your meal plan first in Step 5.")
        else:
            st.markdown("Here’s your grocery list based on the meal plan:")

            grocery_list = {}

            for meal in selected_meals.values():
                meal_name = meal["name"]
                ingredients = ingredient_db.get(meal_name, {})
                for item, qty in ingredients.items():
                    if item in grocery_list:
                        grocery_list[item] = f"{grocery_list[item]} + {qty}"
                    else:
                        grocery_list[item] = qty

            for item, qty in grocery_list.items():
                st.write(f"• **{item}**: {qty}")

        if st.button("🔄 Start Over"):
            st.session_state.step = 1
