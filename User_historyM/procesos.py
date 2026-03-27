from validate_options import validate_input_product_name, validate_input_price, validate_input_quantity
#Procesos del menu 
#agregar las caracteristicas del producto,nombre, cantidad y precio
def add_product(inventory):
    name_product = validate_input_product_name()
    price = validate_input_price()
    quantity = validate_input_quantity()

    product = {
        "name_product": name_product, 
        "price": price,
        "quantity": quantity,
    }    

    inventory.append(product)


def calculate_statistics(inventory):
    total=0
    summary_product = 0
    for product in inventory: 
       total+= product ['price'] * product ['quantity'] 
       summary_product += product ['quantity']

    print(f"el total  de venta es: {total}")
    print(f"la cantidad total de productos vendidos: {summary_product}")





def show_inventory(inventory):
    if not inventory:
        print ("Inventory empty")
        return


    for product in inventory:
        print("---------------------------------------------------")
        print(f"The name of the product is: {product['name_product']}")
        print(f"The price of the product is: {product['price']}")
        print(f"The quantity of the profuct is: {product['quantity']}")
        print("---------------------------------------------------")
    
