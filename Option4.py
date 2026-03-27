

def product_update(Inventory, name):
    VALIDATOR = True
    VALIDATOR_FALSE = False
    VALIDATOR_X =False
    # Verifica si existe el producto
    producto = Inventory.get(name)
    
    if not producto:
        print(f" Product '{name}' not found.")
        return VALIDATOR_FALSE
    

    print(f"\nUpdate: {name} (Price: {producto['price']}, Stock: {producto['quantity']})")
    print("1. Change Price")
    print("2. Change Stock")
    print("3. Change Both")
    
    option = input("Choose an option: ")

    if option == "1":
        producto["price"] = float(input("New price: "))
    elif option == "2":
        producto["quantity"] = int(input("New stock: "))
    elif option == "3":
        producto["price"] = float(input("New price: "))
        producto["quantity"] = int(input("New stock: "))
    else:
        print("Invalid option.")
        return VALIDATOR_X

    print(" Update successful.")
    return VALIDATOR




















# import Option2

# def actualizar_producto(name, key, new_value):
#     # 'key' será "price" o "quantity"
#     VALIDATOR = True
#     VALIDATOR_FALSE = False
#     if name in Option2.Inventory:
#         Option2.Inventory[name][key] = new_value
#         return VALIDATOR
#     return VALIDATOR_FALSE
#     #----------------------------------------------------
    