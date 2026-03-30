from process import add_product, show_inventory, search_product, update_product, delete_product, calculate_statistics
from files import save_csv, load_csv, ask_load_action, overwrite_inventory, merge_inventory


def menu(): 
    validate = True #variable to control the menu loop
    inventory = [] #list empty to save the products in the inventory
    while validate:
        print("----------------")
        print("Welcome to menu")
        print("----------------")
        print("1- Add product")
        print("2- Show history purchase")
        print("3- Search product")
        print("4- Update product")
        print("5- Delete product")
        print("6- Calculate statistics")
        print("7- Save inventory to CSV")
        print("8- Load inventory from CSV")
        print("9- Exit")
        
        option = input("Please choose an option: ")
        if option == "1":
            add_product(inventory)
        
        elif option == "2":
            show_inventory(inventory)

        elif option == "3":
            search_product(inventory)

        elif option == "4":
            update_product(inventory)
        
        elif option == "5":
            delete_product(inventory)

        elif option == "6":
            calculate_statistics(inventory)

        elif option == "7":
            path = input("Enter filename (default: inventory.csv): ").strip() 
            if not path:
                path = "inventory.csv"
            save_csv(inventory, path)

        elif option == "8":
            path = input("Enter filename to load (default: inventory.csv): ").strip()
            if not path:
                path = "inventory.csv"
            
            inventory_load = load_csv(path)
            if inventory_load is not None:
                accion = ask_load_action()
                if accion == 'overwrite':
                    inventory = overwrite_inventory(inventory, inventory_load)
                    print(f"Inventory overwritten. Total of products: {len(inventory)}\n")
                elif accion == 'merge':
                    print("Merging inventory...")
                    inventory, fusionados, nuevos = merge_inventory(inventory, inventory_load)
                    print(f"\nSummary: {fusionados} products updated, {nuevos} new products added.")
                    print(f"Total of products in inventory: {len(inventory)}\n")

        elif option == "9":
            print("Exit the system. Thank for using it")
            validate = False
        else:
            print("Invalid option, please choose a number from 1 to 9.")        



 
        

