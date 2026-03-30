from validate_options import validate_input_product_name, validate_input_price, validate_input_quantity, validate_product_name_unique
#menu options. 

#function to add product details: name, quantity, and price
def add_product(inventory): 
    name_product = validate_input_product_name()
    
    while not validate_product_name_unique(name_product, inventory): #while the name is not unique, it will keep asking for new name. 
        print(f"ERROR: Product '{name_product}' already exists in the inventory. Please enter a different product name.")
        name_product = validate_input_product_name()  

    price = validate_input_price()
    quantity = validate_input_quantity()

    product = {
        "name_product": name_product, 
        "price": price,
        "quantity": quantity,
    }    

    inventory.append(product)

def calculate_statistics(inventory): #funtion to calculate statistics of the inventory
    total=0
    summary_product = 0
    for product in inventory: 
       total+= product ['price'] * product ['quantity'] 
       summary_product += product ['quantity']

    expensive_product = inventory[0] 
    highest_stock_product = inventory[0]
    # Recorrer inventario
    for product in inventory:
        # Validar producto más caro
        if product.get('price', 0) > expensive_product.get('price', 0):
            expensive_product = product

        # Validar mayor stock
        if product.get('quantity', 0) > highest_stock_product.get('quantity', 0):
            highest_stock_product = product

    # Show results statistics
    print("\n========== STATISTICS ==========")
    
    print(f"Total sales: {total}")
    print(f"Total quantity of products sold: {summary_product}")
    print(f"Most expensive product: {expensive_product.get('name_product')} - ${expensive_product.get('price')}")
    print(f"Highest stock product: {highest_stock_product.get('name_product')} - {highest_stock_product.get('quantity')} units")
    print("================================\n")



def show_inventory(inventory):
    if not inventory:
        print ("Inventory empty")
        return


    for product in inventory:
        print("---------------------------------------------------")
        print(f"The name of the product is: {product['name_product']}")
        print(f"The price of the product is: {product['price']}")
        print(f"The quantity of the product is: {product['quantity']}")
        print("---------------------------------------------------")

def search_product(inventory):
    found = False
    if not inventory:
        print("Inventory empty. Add products first.")
        return

    query = input("Enter product name to search: ").strip().lower() #query is key of name product to search in inventory
    if query == "":
        print("Search query cannot be empty.")
        return

   
    for product in inventory:
        if product['name_product'].strip().lower() == query:
            found = True
            print("---------------------------------------------------")
            print(f"The name of the product is: {product['name_product']}")
            print(f"The price of the product is: {product['price']}")
            print(f"The quantity of the product is: {product['quantity']}")
            print("---------------------------------------------------")

    if not found:
        print(f"No product found with name '{query}'.")

def update_product(inventory): 
    found = False
    if not inventory:
        print("Inventory empty. Add products first.")
        return

    query = input("Enter the name of the product to update: ").strip().lower()
    if query == "":
        print("Product name cannot be empty.")
        return

    for product in inventory:
        if product['name_product'].strip().lower() == query: #for used the query to search the product in inventory to update
            found = True
            print("---------------------------------------------------")
            print(f"Current product: {product['name_product']}")
            print(f"Current price: {product['price']}")
            print(f"Current quantity: {product['quantity']}")
            print("---------------------------------------------------")
            
            print("\nWhat do you want to update?")
            print("1- Price")
            print("2- Quantity")
            
            option = input("Please choose an option: ")
            
            if option == "1":
                product['price'] = validate_input_price()
                print("Price updated successfully.")
                
            elif option == "2":
                product['quantity'] = validate_input_quantity()
                print("Quantity updated successfully.")
                
            else:
                print("Invalid option.")
            
            print("---------------------------------------------------")
            print(f"Updated product: {product['name_product']}")
            print(f"New price: {product['price']}")
            print(f"New quantity: {product['quantity']}")
            print("---------------------------------------------------")
            return

    if not found:
        print(f"No product found with name '{query}'.")

def delete_product(inventory): #function to delete a product from the inventory
    found = False
    if not inventory:
        print("Inventory empty. Add products first.")
        return

    query = input("Enter the name of the product to delete: ").strip().lower() #query is key of name product to search in inventory to delete
    if query == "":
        print("Product name cannot be empty.")
        return

    for product in inventory:
        if product['name_product'].strip().lower() == query:
            found = True
            inventory.remove(product)
            print(f"Product '{query}' deleted successfully.")
            return

    if not found:
        print(f"No product found with name '{query}'.")
