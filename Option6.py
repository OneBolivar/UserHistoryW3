

def calculate_statistics(Inventory):
    # 1. Fetch the inventory from the other module
    product_added = {}
    product_added.update(Inventory)

    if not product_added:
        print("\n The inventory is empty.")
        return

    # 2. Use a lambda to calculate the subtotal
    # Usage: calculate_subtotal(product_data)
    calculate_subtotal = lambda d: d['price'] * d['quantity']

    # Sum quantities and subtotals by iterating through the dictionary
    total_units = sum(d['quantity'] for d in product_added.values())
    total_value = sum(calculate_subtotal(d) for d in product_added.values())

    # 4. Find featured products using 'max' and a lambda
    # We search in items (name, data) based on price or quantity
    expensive_name, expensive_data = max(product_added.items(), key=lambda item: item[1]['price'])
    stock_name, stock_data = max(product_added.items(), key=lambda item: item[1]['quantity'])

    # 5. Display statistics in a readable format
    print("\n---------------------------------------------------------")
    print("                INVENTORY STATISTICS")
    print("---------------------------------------------------------")
    print(f"Total units:          {total_units}")
    print(f"Total value:          ${total_value:,.2f}")
    print(f"Most expensive:       {expensive_name} (${expensive_data['price']})")
    print(f"Highest stock:        {stock_name} ({stock_data['quantity']} units)")
    print("---------------------------------------------------------")
