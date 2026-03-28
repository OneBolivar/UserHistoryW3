import csv



def save_csv(Inventory_to_csv, route='inventory.csv'):
   if not  Inventory_to_csv: 
      print("No information has been saved")
      return
   try:
      with open(route,'w', newline='', encoding='utf-8') as csvfile:
         fieldnames=['Product','Price','Quantity']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         writer.writeheader()
         writer.writerows( Inventory_to_csv)
      return f"\nInventory stored in: {route}"

   except FileExistsError :
      print("The csv file could not be saved")

# this feature is used to upload a csv file to a specific location 
