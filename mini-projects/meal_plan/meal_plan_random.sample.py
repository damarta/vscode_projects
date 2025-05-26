import random

# Step 1:   Create a define meals
breakfast_options = ["Protein Carrot cake", "Protein shake", "Protein Taco"]
lunch_options = ["Protein Chicken Taco", "Protein shake", "Smoothie Fruits", "Protein Carrot cake"]
dinner_options = ["Rise with chicken", "Protein Pokebol", "Protein Pizza"]

# Step 2:   Define the function
def sample_meal_plan():

    breakfast = random.sample(breakfast_options, k=1)[0]
    lunch = random.sample([ m for m in lunch_options if m != breakfast], k=1)[0]
    dinner = random.sample([ m for m in dinner_options if m not in [breakfast, lunch]], k=1) [0]

    print("\n🍽️ Meal plan for today:")
    print(f"  🥣 -Breakfast: {breakfast}")
    print(f"  🥪 -Lunch: {lunch}")
    print(f"  🍛 -Dinner: {dinner}")

# Step 3:   Loop
while True:
    sample_meal_plan()

    again = input("\nDo you want another meal plan? (yes/no) ").lower()

    if again != "yes":
        print("Bon apetit")
        break