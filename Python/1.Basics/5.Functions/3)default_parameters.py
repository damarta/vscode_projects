""" --- Default Parameters --- """

# what's a default parameter ?
    # - given default values to paramaters in a function.
    # - # if we don't pass a value, the default value will be used.

# ##-----------------------------------------------------------

    # -- example 1 --
def greet_user(name = "luis"):
    print(f"Hello, {name}. How are you today ?")

greet_user()
greet_user("Benthe")
# ##-----------------------------------------------------------


    # -- example 2 --
def user(name = "user"):
    return f"Hello, {name}!"
user1 = user()
user2 = user("Luis")
print(user1)
print(user1, user2)

# ##-----------------------------------------------------------

    # -- example 3 --
def fav_food(food= "pizza"):
    print(f"My favorite food is {food}.")

fav_food()
fav_food("sushi")
fav_food("pasta")

# ##-----------------------------------------------------------

    # -- example 4 --
def fav_color(color= "red", name = "Luis"):
    return f" My name is {name} and favorite color is {color}."

fav_1=fav_color()
fav_2=fav_color(name = "Benthe", color = "orange")

print(fav_1)
print(fav_2)