VALIDATOR_NAME = True
while VALIDATOR_NAME:
        product_name = input("Enter the product name: ").strip()
        if product_name == "":
            print("ERROR! Name cannot be empty.")
        else:
            VALIDATOR_NAME = False 
VALIDATOR_PRICE = True
while VALIDATOR_PRICE:
        try:
            product_price = float(input("Enter the product price: "))
            if product_price < 0:
                int("Force Error") 
            else:
                VALIDATOR_PRICE = False 
        except ValueError:
            print("ERROR! Invalid price (must be a positive number). Try again.")
VALIDATOR_QUANTITY = True
while VALIDATOR_QUANTITY:
        try:
            product_quantity = int(input("How many products do you want to buy?: "))
            if product_quantity < 0:
                int("Force Error")
            else:
                VALIDATOR_QUANTITY = False 
        except ValueError:
            print("ERROR! Invalid quantity (must be a positive integer). Try again.")
total = product_price * product_quantity
print(f"Product: {product_name} | Unit Price: {product_price} | Quantity: {product_quantity} | Total to pay: {total}")


   