#Procesos del menu 
#agregar las caracteristicas del producto,nombre, cantidad y precio
def add_product(inventory):
    name_product = input("Add product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = {
        "name_product": name_product, 
        "price": price,
        "quantity": quantity,
    }    

    inventory.append(product)
    print(f"{name_product}succesfully added")


def calculate_statistics(inventory):
    if not inventory:
        print("Inventory is empty. No statistics to show. ")
        return
    
    total=0
    summary_product = 0
    for product in inventory: 
       total+= product ['price'] * product ['quantity'] 
       summary_product += product ['quantity']





def show_inventory(inventory):
    if not inventory:
        print ("Inventory empty")
        return


    for product in inventory:
        print("---------------------------------------------------")
        print(f"The name of the product is: {product['name_product']}")
        print(f"The price of the product is:{product['price']}")
        print(f"The quantity of the profuct is:{product['quantity']}")
        print("---------------------------------------------------")
    
    #revisar porque no esta ahora mostrando bien los resultados :(