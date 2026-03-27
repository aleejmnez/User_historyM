#definition of functions: 

#definition of postive number 
#this function control that numbers less than 0 are no placed. 
def ask_number_postive(message):
    validate = True
    while validate:
        number = int(input(message))
        if number > 0:
            validate = False
        else:
            print("Error: Negative numbers are not allowed. Please try again. ")

    return number

#definition of empty string. 
#this function control that the user not input emptry string
def validate_empty_string(message):
    validate = True
    while validate: 
        string = input(message).strip()
        if string: 
            validate = True
    else: 
        print("Error: Not empty string allowed. PLease try again. ")

################################################################################
#estas funciones las debo crear 

def validate_input_product_name():
    user_input = input("Enter the name of the product: ")
    while user_input.strip() == "":
        print("ERROR: Product name cannot be empty. Please enter a valid product name.")    
        user_input = input("Enter the name of the product: ")

    return user_input.strip()

def validate_input_price():
    validate =True
    while validate: 
        try:
            price = float(input("Enter the price of the product: "))
            if price < 0:
                print("ERROR: Price cannot be negative. Please enter a valid price.")
                
            elif price == 0:
                print("ERROR: Price cannot be zero. Please enter a valid price.")
              
            else:
                validate = False
                return price
        except ValueError:
            print("ERROR: Please enter a valid numeric value for price.")
            
                   
def validate_input_quantity():
    validate = True
    while validate:
        try:
            quantity = int(input("Enter the quantity sold: "))
            if quantity < 0:
                print("ERROR: Quantity cannot be negative. Please enter a valid quantity.")
            elif quantity == 0:
                print("ERROR: Quantity cannot be zero. Please enter a valid quantity.")    
          
            else:
                validate = False
                
        except ValueError:
            print("ERROR: Please enter a valid numeric value for quantity.")   
    return quantity
                   
def record_sales2(): #This funcition only catch the variables, doesn't make the historial's record sales
    try:    
        print("Sales recorded successfully.")
        record_sales = {}
        producto_name = input("Enter the name of the product: ")
        producto_name = validate_input_product_name(producto_name)
        Producto_price = input("Enter the price of the product: ")
        Producto_price = validate_input_price(Producto_price)
        quantity = input("Enter the quantity sold: ")
        quantity = validate_input_quantity(quantity)

        total_sale = Producto_price * quantity
        record_sales[producto_name] = {
            "price": Producto_price,
            "quantity": quantity,
            "total_sale": total_sale
        }
        return record_sales
    except ValueError:
        print("ERROR: Please enter valid numeric values for price and quantity.")

def record_sales_print():
    validate_record = True
    total_records = {}
    while validate_record:
        decision = input("Do you want to record a sale? (yes/no): ").strip().lower()
        if decision == 'no':
            total_records_day = sum(details['total_sale'] for details in total_records.values())
            print("---------------------------------------------------------")
            print("Thank you for using the sales recording system.")
            print("Here are the recorded sales:")
            for product, details in total_records.items():
                print(f"Product: {product}")
                print(f"  Price: {details['price']}")
                print(f"  Quantity: {details['quantity']}")
                print(f"  Total Sale: {details['total_sale']}")
            print("---------------------------------------------------------")
            print(f"Total sales recorded for the day: {total_records_day}")
            print("---------------------------------------------------------")
            print("Exiting the sales recording system.")
            
            validate_record = False
        elif decision == 'yes':
            total_records.update(record_sales2())
            print("Sales recorded successfully.")
            print("---------------------------------------------------------")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return
