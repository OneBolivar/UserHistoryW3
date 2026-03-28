 
def inventory_print(Inventory): # Defines the function that will print the inventory content
    product_added = {} # Creates a temporary local dictionary
    product_added.update(Inventory) # Copies the global inventory content to the local dictionary
    print("---------------------------------------------------------") # Prints a decorative line
    print("Here are your inventory") # Shows the inventory report header
    for product, details in product_added.items(): # Starts a loop to go through each product and its details
        print(f"Product: {product}") # Prints the current product name
        print(f"  Price: {details['price']} by unit") # Prints the unit price of the product
        print(f"  Quantity: {details['quantity']}") # Prints the available quantity of the product

    print("---------------------------------------------------------") # Prints a closing decorative line
    print("---------------------------------------------------------") # Prints a second decorative line
    print("Exiting the inventory management system.") # Shows exit message from the management system
    print(" ") # Prints a blank space to improve readability
    return # Ends the execution of the function and returns to the menu
