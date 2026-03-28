from Option1 import OptionNumber1 # Imports the OptionNumber1 function from the Option1 module
from Option2 import inventory_print # Imports the function to print the inventory from Option2
import Option2 # Imports the complete Option2 module to access its variables
from Option3 import product_search # Imports the search function from the Option3 module
import Option4 # Imports the complete Option4 module to access its variables
import Option5 # Imports the complete Option5 module to access its variables    
from Option6 import calculate_statistics # Imports the statistics function from the Option6 module
from Option7 import save_csv
from Option8 import upload_inventory_csv



def MenuOptions(): 
    # MAIN CONTROL: Initialize the central data structures
    Inventory = {} # Creates an empty global dictionary to store all products
    Inventory_to_csv=[]  # List for CSV export
    VALIDATOR = True 
    while VALIDATOR: # Starts the loop that will repeat the menu until exit is selected
        print("                   Welcome") 
        print("=" * 50) 
        print("=" * 50) 
        print("1. Add product") 
        print("2. Show inventory") 
        print("3. Search product") 
        print("4. Update product") 
        print("5. Delete product") 
        print("6. Calculates statistics")
        print("7. Save CSV")
        print("8. Upload CSV") 
        print("9. Exit") 
        
        #---------------------------------------------------------
        # INPUT VALIDATION: Ensure user selects valid menu option (1-9)
        VALIDATOR_OPTIONS = True # Variable to validate user input
        try: # Starts error handling block (in case the user enters letters)
            while VALIDATOR_OPTIONS: 
                Options = float(input("What do you want to do?: "))
                print("      ") 
                # VALIDATION: Check if option is in valid range
                if (Options <= 0) or (Options > 9): 
                    int("Force Error") # If the number is invalid, forces an error to go to except
                elif Options == 1: 
                    OptionNumber1(Inventory, Inventory_to_csv) 
                   
                elif Options == 2: 
                    inventory_print(Inventory) # Calls the function that displays the products on screen
                elif Options == 3:
                    product_name = input("Enter the name of the product you wish to search for: ")
                    resultado = product_search(product_name, Inventory)
                    if resultado != {}:
                        print(f"Product Found: {resultado}")
                    else:
                        print("The product doesn't exist in the inventory")
                elif Options == 4:
                    name = input("What product do you want to update?: ")
                    Option4.product_update(Inventory, name)
                elif Options == 5:
                    Option5.product_delete(Inventory)
                elif Options == 6:
                    calculate_statistics(Inventory) # Executes the function that processes numerical data
                elif Options == 7:
                   print(save_csv( Inventory_to_csv))
                elif Options == 8:
                    upload_inventory_csv(Inventory)                                   
                elif Options == 9: 
                    print("Thank you so much for using our system, have a nice day") 
                    VALIDATOR_OPTIONS = False
                    VALIDATOR = False
         
        #------------------------------------------------------------        
        # ERROR HANDLING: Catch invalid inputs (non-numeric or out-of-range)
        except ValueError: # Executes if the user enters something that is not a number or an invalid option
            print("---------------------------------------") 
            print("Error only shows the displayed options") # Error message to the user
            print("---------------------------------------") 
            print("    ") 
