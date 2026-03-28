def OptionNumber1(Inventory, Inventory_to_csv):
    # PRODUCT CREATION: Add new items to inventory with full validation
    # Validates: name (non-empty), price (positive float), quantity (positive integer)
    
    # STEP 1: NAME VALIDATION - Must be non-empty string
    VALIDATOR_NAME = True 
    while VALIDATOR_NAME: 
                product_name = input("Enter the product name: ").strip() # Asks for the name and removes extra spaces
                if product_name == "": # Validates if the name is empty
                    print("ERROR! Name cannot be empty. ") # Shows error if nothing was written
                else:
                    VALIDATOR_NAME = False 
    #------------------------------------------------------------
    # STEP 2: PRICE VALIDATION - Must be positive number (converted to float)
    VALIDATOR_PRICE = True # Control variable for the price validation loop
    while VALIDATOR_PRICE: # Starts loop to ensure the price is correct
            try: # Block to attempt to execute code that may fail
                product_price = float(input("Enter the product price: ")) # Converts input to decimal number
                if product_price < 0: # Checks if the price is a negative number
                    int("Force Error") # Forces a manual error to jump to except
                else:
                    VALIDATOR_PRICE = False # Changes the state to exit the price loop
            except ValueError: # Captures data type errors or forced errors
                print("ERROR! Invalid price (must be a positive number). Try again.") # Error message
    #------------------------------------------------------------
    # STEP 3: QUANTITY VALIDATION - Must be positive integer
    VALIDATOR_QUANTITY = True # Control variable for the quantity loop
    while VALIDATOR_QUANTITY: # Starts loop to validate the quantity of products
            try: # Block to capture errors when entering quantity
                product_quantity = int(input("How many products do you want to buy?: ")) # Converts input to integer
                if product_quantity < 0: # Checks if the quantity is negative
                    int("Force Error") # Forces a manual error
                else:
                    
                    print("Product successfully registered") # Confirms the product registration
                    print("  ") # Prints a blank space for visual order
                    VALIDATOR_QUANTITY = False # Changes the state to exit the quantity loop
            except ValueError: # Captures errors if it is not a positive integer
                print("ERROR! Invalid quantity (must be a positive integer). Try again.") # Error message
    
    # STEP 4: STORE DATA - Add product to both Inventory dict and CSV export list
    
    Inventory[product_name]={ # Adds the product name as a key in the dictionary
        "price" : product_price, # Stores the price within the product sub-dictionary
        "quantity" : product_quantity, # Stores the quantity within the product sub-dictionary
    }
    
    Inventory_to_csv.append({
        "Product": product_name,
        "Price": product_price,
        "Quantity": product_quantity
        })
        
    return Inventory , Inventory_to_csv# Returns the dictionary with the registered information
    
