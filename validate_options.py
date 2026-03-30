#definition of functions: 

#definition of positive number 
#this function control that numbers less than 0 are no placed. 
def ask_number_postive(message): 
    validate = True
    while validate:
        try:
            number = int(input(message))
            if number > 0:
                validate = False
            else:
                print("Error: Negative numbers are not allowed. Please try again. ")
        except ValueError:
            print("Error: Please enter a valid integer.")

    return number

#definition of empty string. 
#this function control that the user not input empty string
def validate_empty_string(message):
    string = input(message).strip()
    if not string:
        print("Error: Not empty string allowed. Please try again.")
        return validate_empty_string(message)
    return string

def validate_input_product_name(): #function to validate the product name input successfully
    user_input = input("Enter the name of the product: ").strip()
    if not user_input: #if the user enter empty string, print error 
        print("ERROR: Product name cannot be empty. Please enter a valid product name.")
        return validate_input_product_name()
    elif not user_input.replace(" ", "").isalpha(): #only alphabetic characters
        print("ERROR: Product name can only contain letters. Please enter a valid product name.")
        return validate_input_product_name()
    else:
        return user_input


def validate_product_name_unique(product_name, inventory):
    for product in inventory: #for to check if the product name already exists in the inventory, if exists print error
        if product['name_product'].strip().lower() == product_name.strip().lower():
            print(f"ERROR: Product '{product_name}' already exists in the inventory. Please enter a different product name.")
            return False
    return True


def validate_input_price(): #function to validate the price input 
    try:
        price = float(input("Enter the price of the product: "))
        if price <= 0: #not negative number and not zero
            print("ERROR: Price must be positive and non-zero. Please enter a valid price.")
            return validate_input_price()
        else:
            return price
    except ValueError:
        print("ERROR: Please enter a valid numeric value for price.")
        return validate_input_price()
                   

def validate_input_quantity(): #function to validate the quantity input
    validate = True
    while validate:
        try:
            quantity = int(input("Enter the quantity sold: ")) #not negative number and not zero
            if quantity <= 0:
                print("ERROR: Quantity must be positive and non-zero. Please enter a valid quantity.")
            else:
                validate = False
                
        except ValueError:
            print("ERROR: Please enter a valid numeric value for quantity.")   
    return quantity