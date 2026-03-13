# Initialize validator for name input
VALIDATOR_NAME = True #variable to control the while loop for input validation
while VALIDATOR_NAME:#Start the name validator
        # Get product name from user and remove leading/trailing whitespace
        product_name = input("Enter the product name: ").strip()#input for the name of the item
        if product_name == "":#Conditional to trigger error when user leaves it empty and presses ENTER
            print("ERROR! Name cannot be empty. ")
        else:
            VALIDATOR_NAME = False #If we reach here, the validator becomes FALSE and proceeds to the next line of code
# Initialize validator for price input
VALIDATOR_PRICE = True
while VALIDATOR_PRICE:#Start the price validator
        try:
            # Get product price from user and convert to float
            product_price = float(input("Enter the product price: "))#input for the price of the item, converted to float
            if product_price < 0:#Conditional to trigger error when user enters a negative number
                int("Force Error") #If we reach here, force the error
            else:#Otherwise
                VALIDATOR_PRICE = False #If we reach here, the validator becomes FALSE and proceeds to the next line of code
        except ValueError:#Error: ValueError means a value error
            print("ERROR! Invalid price (must be a positive number). Try again.")#
# Initialize validator for quantity input
VALIDATOR_QUANTITY = True
while VALIDATOR_QUANTITY:
        try:
            # Get product quantity from user and convert to integer
            product_quantity = int(input("How many products do you want to buy?: "))#input for the quantity of the item, converted to int
            if product_quantity < 0:
                int("Force Error")  # Force error for negative quantity
            else:
                VALIDATOR_QUANTITY = False  # Exit the loop if valid 
        except ValueError:
            print("ERROR! Invalid quantity (must be a positive integer). Try again.")
# Calculate total cost of purchase
total = product_price * product_quantity#calculating the total cost of the item
# Display purchase summary with all details
print(f"Product: {product_name} | Unit Price: {product_price} | Quantity: {product_quantity} | Total to pay: {total}")
#This programm will prompt the user to enter the name, price, and quantity of an item, and then it will calculate and display the total cost of the item. 
# The program also includes input validation to ensure that the user enters the correct data types for price and quantity.

   