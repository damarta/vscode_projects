""" 🚀 Mini Project: “Smart Shopping Cart” (Understanding Functions)"""

# This project will help me to understand functions deeply by combining:
    # parameters
    # arguments
    # return
    # default parameters
    # *args
    # **kwargs

#📌 Project Overview
    # We will create a shoppping carts system that allows user to:

        #1) add items to the cart (with dynamic prices).
        #2) view the cart contents.
        #3) calculate the total price.
        #4) Apply optional discount.
        #5) Check-Out the order.
 
#💡 What You Will Learn:
    #✅ Basic Functions (how to define and call functions.)
    #✅ Parameters & Arguments (passing data into functions.)
    #✅ Return Values (Storing functions results.)
    #✅ *args (Handling multiple items dynamically).
    #✅ **kwargs (Managing flexible named arguments).
    #✅ Default parameters (Creating optional values).
    #✅ Scope in Functions (Global vs Local variable).

#📝 Step 2: Setting Up the Shopping Cart
    # we will use  dictionary to store the cxart items and their prices.
shopping_cart ={}

#📝 Step 2: Functions to add items to the cart (*args)
    # we will define a function that adds multiple items at once.
def add_to_cart(*items):
    for item in items:
        name, price = item # each item is a tuple (name, price)
        shopping_cart[name] = price # Store in dictionary
        print(f"Added{name} to cart ${price:.2f}.") # ask?

#🛠 Example Usage
add_to_cart(("Pizza", 10), ("Cola", 3))

#📝 Step 3: Viewing tha cart
    # We will create a function to display the current cart contents.
def view_cart():
    if not shopping_cart:
        print("\n🛒 Your cart is empty!")
    else:
        print("\n🛒 Your Shopping cart:")
        for item, price in shopping_cart.items():
            print(f" - {item}: ${price:.2f}")

#🛠 Example Usage
view_cart()

#📝 Step 4: Functions to calculate Total price
def calculate_total():
    return sum(shopping_cart.values())

#🛠 Example Usage
total = calculate_total()
print(f"💰 Total: ${total:.2f}")

#📝 Step 5: Applying Discounts (**kwargs)
def apply_discount(**kwargs):
    total = calculate_total()
    discount_amount = kwargs.get("discount", 0) # Default: is 0. if no discount is provided.
    total_after_discount = total - discount_amount

    print(f"💸 Discount applied: ${discount_amount:.2f}")
    print(f"💰 New Total: S{total_after_discount:.2f}")
    return total_after_discount

#🛠 Example Usage
apply_discount(discount=1.50)

#📝 Step 6: Checkout and Clear the Cart.
    #Once the user confirms the purchase, the cart should be cleared.
def check_out():
    total = calculate_total()

    if total == 0:
        print("⚠️ Your cart is empty! Add itemd before checking out.")
        return
    print("\n ✅ Purchase successful!")
    print(f"💳 Final Amount Paid: $ {total:.2f}")

    shopping_cart.clear()
    print("🛒 Your cart is now empty.")

#🛠 Example Usage
check_out()


#🎯 What You Learned:
    #✅ How to use *args to accept multiple values.
    #✅ How to use **kwargs to accept optional parameters.
    #✅ How to return and store function results.
    #✅ How to combine multiple functions into a mini-project.
    #✅ How to apply default parameters for flexibility.
    