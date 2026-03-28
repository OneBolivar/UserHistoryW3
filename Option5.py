

def product_delete(Inventory):
    name = input("Enter the name of the product you wish to delete: ")
    VALIDATOR = True
    VALIDATOR_FALSE = False 
    VALIDATOR_X = False
    # We check if it exists in the Option2 inventory
    if name in Inventory:
        confirmar = input(f" Are you sure you want to delete '{name}'? (Yes/No): ").lower()
        
        if confirmar == 'yes':
            del Inventory[name]
            print(f" The product '{name}' has been successfully deleted.")
            return VALIDATOR
        else:
            print(" Operation cancelled by the user")
            return VALIDATOR_FALSE
    else:
        print(f" Error: The product '{name}' does not exist in the inventory.")
        return VALIDATOR_X
    

