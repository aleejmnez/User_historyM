from procesos import add_product,calculate_statistics,show_inventory


def menu():
    validate = True
    inventory = []
    while validate:
        print("----------------")
        print("Welcome to menu")
        print("----------------")
        print("1- Add product")
        print("2- Show history purchase")
        print("3- Calculate statistics")
        print("4- Exit")
        
        option = input("Please choose an option: ")
        if option == "1":
            add_product(inventory)
        
        elif option == "2":
            show_inventory (inventory)

        elif option == "3":
            calculate_statistics(inventory)

        elif option == "4":
            print ("Exit the system. Thank for using it")
            validate = False        



 
        

