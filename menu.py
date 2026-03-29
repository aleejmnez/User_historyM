from procesos import add_product, show_inventory, search_product, update_product, delete_product, calculate_statistics
from archivos import save_csv, load_csv, ask_load_action, overwrite_inventory, merge_inventory


def menu():
    validate = True
    inventory = []
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
            ruta = input("Enter filename (default: inventario.csv): ").strip()
            if not ruta:
                ruta = "inventario.csv"
            save_csv(inventory, ruta)

        elif option == "8":
            ruta = input("Enter filename to load (default: inventario.csv): ").strip()
            if not ruta:
                ruta = "inventario.csv"
            
            inventario_cargado = load_csv(ruta)
            if inventario_cargado is not None:
                accion = ask_load_action()
                if accion == 'overwrite':
                    inventory = overwrite_inventory(inventory, inventario_cargado)
                    print(f"Inventario reemplazado. Total de productos: {len(inventory)}\n")
                elif accion == 'merge':
                    print("Fusionando inventarios...")
                    inventory, fusionados, nuevos = merge_inventory(inventory, inventario_cargado)
                    print(f"\nResumen: {fusionados} productos actualizados, {nuevos} productos nuevos agregados.")
                    print(f"Total de productos en inventario: {len(inventory)}\n")

        elif option == "9":
            print("Exit the system. Thank for using it")
            validate = False
        else:
            print("Invalid option, please choose a number from 1 to 9.")        



 
        

