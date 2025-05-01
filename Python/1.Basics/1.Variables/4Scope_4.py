# In Python you need to understand how can you use 'variables' or how you can call them.

# Variables: 
    # 1. Assignment : 


    # 2. Naming Conventions:


    # 3. Scope:
        # - Where can you use your variables?

""" Global: Variables created outside of the function  """

x = 10 # global variable

def print_number():
    print(x) # can access global varibales

print_number() # 10

# ---- the function have access the global variable x.

# --------------------------------------------------------------------------------



"""  Local: Variables created inside of the function  """
                 
def my_funtion():
    y = 5
    print(y)

my_funtion () # 5
# print (y) outside of the function will give you a error.

# --------------------------------------------------------------------------------



""" ---- Global vs Local Variables Example: --- """

c = 50

def change_variable():
    c = 10
    print("inside function: ", c)

change_variable()
print("outside function: ", c)
# --------------------------------------------------------------------------------


""" ---- Using Global Keywoird --- """
count = 0

def increment():
    global count
    count += 1
    
increment()
print(count)