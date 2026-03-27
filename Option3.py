# Importa el módulo Option2 para poder acceder al inventario global

def product_search (product_name, Inventory):
    return Inventory.get(product_name, {})