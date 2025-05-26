# #random = to randomly pick meals
# import random

# #json = to save/load data in a file
# import json

# #datetime = to include the current date/time in your saved plan
# from datetime import datetime

# # Inside meal_return.py
# breakfast_options = ["Oatmeal", "Smoothie", "Protein Pancake", "Boiled eggs", "Greek yogurt"]
# lunch_options = ["Chicken wrap", "Sushi", "Grilled tofu", "Veggie bowl", "Tuna pasta"]
# dinner_options = ["Steak", "Chickpea curry", "Salmon", "Pizza", "Stuffed peppers"]

# # Step 3: Create a function that returns a meal plan using sample()
# def generate_unique_meal_plan():
#     breakfast = random.sample([breakfast_options, 1]) [0]
#     lunch = random.sample([ m for m in lunch_options if m != breakfast], 1)[0]
#     dinner = random.sample([m for m in dinner_options if m not in [breakfast, lunch]], 1)[0]
    
#     return {
#         "Breakfast": breakfast,
#         "Lunch": lunch,
#         "Dinner": dinner,
#         "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }

# # step 4: Create a function to save that meal to a JSON file.
# def save_to_json(meal_plan, filename="meal_history_sample.json"):
#     try:
#         with open (filename, "r") as f:
#             data = json.load(f)     # Load existing meal plans (list)
#     except FileNotFoundError:
#         data = []       # If file doesn't exist yet, start fresh

#     data.append(meal_plan)      # Add this new plan

#     with open(filename, "w") as f:
#         json.dump(data, f, indent=2)       # save updated list back into file

# # Step 5: Use loop to run it
# while True:
    
#     meal_plan = generate_unique_meal_plan()
#     print("\nYour unique meal plan for today: ")

#     for key,value  in meal_plan.items():
#         print(f"{key}: {value}")

#     save_to_json(meal_plan)

#     again = input("\nDO you want another meal plan? (yes/no): ").lower()
#     if again != "yes":
#         print("Bon apetit")
#         break


#🧩 Exercise 1: Return + Sample + JSON


    # Step 1: import the required tools
import random
import json
from datetime import datetime

    # Step 2: Create the meal options (list)

breakfast_option = ["protein shake", "Protein carret cake", "Protein ice cream", "protein pancake", "Protein avocado with bread"]
lunch_option = ["protein shake", "Protein carret cake", "Protein ice cream", "protein pancake", "Protein avocado with bread"]
dinner_option = ["Pizza with high protein", "Poke bol with salm", "chicken with rice", "Bistec"]

    # Step 3: Create a function that return a meal plan using sample()

def generate_unique_meal_plan():

    breakfast = random.sample(breakfast_option, 1)[0]    		                                # random.sample(..., 1)[0] -> picks 1 item from the list, no duplicates
    lunch = random.sample([ m for m in lunch_option if m != breakfast], 1)[0]                   # [m for m in 'list_name' if condition]: this is a filter to exclude repeated meals
    dinner = random.sample([ m for m in dinner_option if m not in [breakfast, lunch]], 1)[0]    # [m for m in 'dinner_option' if condition]: this is a filter to exclude repeated meals

    return {
        "Breakfast": breakfast,
        "Lunch": lunch,
        "Dinner": dinner,

        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

