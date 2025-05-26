#1. 🍽️ Project #1: Basic Meal Plan Generator

# 🧠 What You'll Practice:
    # -Lists

    # -random.choice()

    # -Functions

    # -Loops & input()

# Step 0:
import random

# Step 1:   Define meal options.
breakfast_options = ["Protein Carrot cake", "Protein shake", "Protein Taco"]
lunch_options = ["Protein Chicken Taco", "Protein shake", "Smoothie Fruits", "Protein Carrot cake"]
dinner_options = ["Rise with chicken", "Protein Pokebol", "Protein Pizza"]

# Step 2:   Define a function to generate the meal plan.
def generate_meal_plan():
    breakfast = random.choice(breakfast_options)
    lunch = random.choice(lunch_options)
    dinner = random.choice(dinner_options)

    print(f"\n🍽️ Here's your meal plan for today: ")
    print(f"🥣 Breakfast: {breakfast}")
    print(f"🥪 Lunch: {lunch}")
    print(f"🍛 Dinner: {dinner}")

# Step 3:   Loop for repeated use.
while True:
    generate_meal_plan()
    again = input("\nDo you want another meal plan for today? (yes/no)").lower()

    if again != "yes":
        print("Bon appetit!")
        break
