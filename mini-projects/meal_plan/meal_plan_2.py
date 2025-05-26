#🛠️ Two Upgrades:

    #- Allow user to add 2 custom meal options per category (and store them for this session)
    #- Add dietary filter like: High Protein, Vegetarian, No filter


        #✅ Upgrade 1: Add Custom Meals
            #Here's how we'll do it:
                #- Ask the user to add 2 meals for each type
                #- Append them to the existing list
                #- Then proceed as usual

        #✅ Upgrade 2: Dietary Filters
            # - We'll tag each meal with a dietary label (like a tuple or dict), 
            #  and then filter the list based on the user's choice.

# </>  Code:

import random

        # Meals with dietary tags:
breakfast_options = [
    ("Protein shake", "High Protein"),
    ("Protein Carrey cake", "Vegan High Protein"),
    ("Pizza", "Fat")
]

lunch_options = [ #list
    ("Protein shake", "High Protein"), # tuple
    ("Protein Carrey Cake", "Vegetarian"),
    ("Chicken Rap", "High Protein"),
    ("Chicken Burrito meal", "High Protein")
]

dinner_options = [
    ("Pizza", "Fat"),
    ("Protein Carrey Cake", "Vegetarian"),
    ("Chicken Rap", "High Protein"),
    ("Chicken Burrito meal", "High Protein")
]

def add_custom_meals(options_list, category_name):
    print(f"\n > Add 2 custom {category_name} options:")

    for _ in range(2):
        name = input(f"Enter a {category_name} item: ")
        tag = input("Is it 'High Protein', 'vegetarian', or 'Fat'? ")
        options_list.append((name,tag))

def filter_meals(options_list, diet_tag):

    if diet_tag == "Fat":
        return options_list
    
    return [meal for meal in options_list if meal[1].lower() == diet_tag.lower()]

def generate_meal_plan(dietary_filter):

    bf = random.choice( filter_meals (breakfast_options, dietary_filter) )
    ln = random.choice( filter_meals (lunch_options, dietary_filter) )
    dn = random.choice( filter_meals (dinner_options, dietary_filter) )

    print("\n Your Meal Plan for Today: ")
    print(f"  -> Breakfast: {bf[0]} ({bf[1]}) ")
    print(f"  -> Lunch: {ln[0]} ({ln[1]})")
    print(f"  -> Dinner: {dn[0]} ({dn[1]})")

        # Add custom meals:
add_custom_meals(breakfast_options, "Breakfast")
add_custom_meals(lunch_options), "Lunch"
add_custom_meals(dinner_options, "Dinner")

        # Choose dietary filter:
diet = input("\nChoose dietary filter (High Protein / Vegetarian / Fat): ")

        # General plan loop:

while True:

    generate_meal_plan(diet)
    again = input("\nWould you like another meal plan (yes/no): ").lower()
    
    if again != 'yes':
        print(" Boon Appeteit!")
        break