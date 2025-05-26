# 🧠 Goal: 

"""Build a program that create a randomized daily meal plan with breakfast, lunch, and dinner using pre-defined
    lists of food options"""

# 🧪 Concepts You'll Practice:

    #- List & indexing
    #- Random selection (random.choice)
    #- Functions
    #- Simple user interaction.

#🧾 Step-by-Step Plan:

    # - Define 3 lists: breakfast_options, lunch_options, and diner_options.
    # - Use random.choice() to pick one item from each list.
    # - Print out the meal plan.
    # - (optional bonus) ask user if they want to generate another plan.

# </> Code:
import random

    # - Step 1: Define meal options
breakfast_options = ["Protein shake", "Protein Carrey Cake", "Pizza"]
lunch_options = ["Protein shake", "Protein Carrey Cake", "Chicken Rap", "Chicken Burrito meal"]
dinner_options  = ["Pizza","Protein Carrey Cake", "Chicken Rap", "Chicken Burrito meal"]


def generate_meal_plan():
    breakfast = random.choice(breakfast_options)
    lunch = random.choice(lunch_options)
    dinner = random.choice(dinner_options)

    print("\n🍽️ Your Meal Plan for Today:")
    print(f"  -Breakfast: {breakfast}")
    print(f"  -Lunch: {lunch}")
    print(f"  -Dinner: {dinner}")

    # - Step 2: Loops for repeated plans.
while True:
    generate_meal_plan()
    again = input("\n >Would you like another meal plan? (yes/no)").lower()

    if again != 'yes':
        print("Bon apetit")
        break

