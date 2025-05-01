""" --- 🔍 **kwargs ---"""

# --- what's --- ?
    # 🔹 **kwargs allows a function to accept any number of named arguments.
    # 🔹(key-value-pairs)
    # 🔹inside of the function, **kwargs acts as a dictionary where the keys are arguments names, and values are the corresponding values.
    # 🔹It is useful when handeling optional arguments or when we don't know in advance what arguments will be passed.

##################################################################################

# -- example 1 ) Basic Example of **kwargs --
  #{CODE}
def display_info(**info):
    print(info) # 🔍: **kwargs is a dictionary
display_info(name = "A", age = 1, city = "H", country = "NL") 
      # 🖥️ Output: {'name': 'A', 'age': 1, 'city': 'H', 'country': 'NL'}

# 📌 Explanation:
   # - Let's define a {function} that accepts {multiple named arguments}.
   # - The function receives multiple named arguments(name, age, country).
   # - **kwargs groups them into a dictionary.
   # - using in this way, you don't print each argument in a dinamically way(you need to use a loop).
  

#####################################################################################

# -- example 2) Looping Through **kwargs--
  #{CODE}
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
display_info(name ="Luis", age = 29, city = "Hilversum", country = "NL")
    # 🖥️ Output:
        # name: Luis
        # age: 29
        # city: Hilversum
        # country: NL

# 📌 Explanation:
   # - Since **kwargs is a dictionary, we can iterate over it.
   # - The function takes multiplw named arguments.
   # - **info.items(), returns {key-value pairs}.
   # - The loop prints each argument dynamically.

#####################################################################################

# -- example 3 ) Using **kwargs for flexibel Functions. --
  #{CODE}
def greet_users(**users):
    for name, greeting in users.items():
        print(f"{greeting}, {name}.")

greet_users(Luis = "Hello", Benthe = "Hello Mw", Kai = "Hello Doggie")
    # 🖥️ Output:
    # Hello, Luis.
    # Hello Mw, Benthe.
    # Hello Doggie, Kai.


# 📌 Explanation:
   # - You can pass any number of named arguments to a function.
   # - Each key (Luis, Benthe, Kai) represents a name.
   # - Each value (hello, hello mw, hello doggie) represents a greeting.
   # - The function prints personalized greetings for each name.


#####################################################################################

# -- example 4) Using **kwargs with defaul values --
  #{CODE}
def configure_settings(**kwargs):
    settings = {
        "theme": kwargs.get("theme", "dark"),
        "language": kwargs.get("language", "English"),
        "notifications": kwargs.get("notifications", True)
    }
    return settings

config = configure_settings(theme = "light", language = "Dutch", notifications = False)
print(config)

print(configure_settings())
    # 🖥️ Output:
    # {'theme': 'light', 'language': 'Dutch', 'notifications': False}
    # {'theme': 'dark', 'language': 'English', 'notifications': True}
# 📌 Explanation:
   # - We can provide default values for missing arguments.
   # - if the user doesn't provide a value, the function uses the default.
   # - Kwarg.get("key", default_value) avoids errors if the key is missing.
   # - The function returns a dictionary with the settings.
#####################################################################################
# -- example 5) Using **kwargs with others Parameters --
  #{CODE}
def intro_person(user_num, name, age, **additional_info):
    
    print(f"User number: {user_num}")
    print(f"Name: {name}")
    print(f"Age: {age}")

    for key, value in additional_info.items():
      print(f"{key.capitalize()}: {value}")

intro_person(1, "Luis", 29, city = "Hilversum", country = "NL", job = "Entrepeneur in HealthTech.")
intro_person(2, "Benthe", 26, city = "Hilversum", country = "NL", job = "Behavior Analyst.")
    # 🖥️ Output:

    # User number: 1
    # Name: Luis
    # Age: 29
    # City: Hilversum
    # Country: NL
    # Job: Entrepeneur in HealthTech.

    # User number: 2
    # Name: Benthe
    # Age: 26
    # City: Hilversum
    # Country: NL
    # Job: Behavior Analyst.
    
# 📌 Explanation:
   # - You can combine **kwargs with normal parameters.
   # - The function requieres user number, name and age.
   # - {** additional_info}, collects extra arguments into a dictionary.
   # - The loop prints the additional information.

#####################################################################################
# -- example 6 ) Combining *args and **kwargs --
  #{CODE} : You can use *args and **kwargs together.

def print_info(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)
print_info(1, 2, 3, name = "Luis", age = 29, city = "Hilversum")
    # 🖥️ Output:
    # Positional Arguments: (1, 2, 3)
    # Keyword Arguments: {'name': 'Luis', 'age': 29, 'city': 'Hilversum'}

# 📌 Explanation:
   # - *args (positioal arguments)
#####################################################################################
