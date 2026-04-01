from process import add_name, show_students, search_students, update_students, delete_students
from files import save_csv, load_csv, ask_load_action, overwrite_inventory, merge_inventory


def menu(): 
    validate = True #variable to control the menu loop
    inventory = [] #list empty to save the products in the inventory
    while validate:
        print("----------------")
        print("Welcome to menu")
        print("----------------")
        print("1- Add name of the students")
        print("2- Show history of the students")
        print("3- Search students")
        print("4- Update students")
        print("5- Delete students")
        print("6- Save inventory to CSV")
        print("7- Exit")
        
        option = input("Please choose an option: ")
        if option == "1":
            add_name(inventory)
        
        elif option == "2":
            show_students(inventory)

        elif option == "3":
            search_students(inventory)

        elif option == "4":
            update_students(inventory)
        
        elif option == "5":
            delete_students(inventory)


        elif option == "6":
            path = input("Enter filename (default: inventory.csv): ").strip() 
            if not path:
                path = "inventory.csv"
            save_csv(inventory, path)

        elif option == "7":
            print("Exit the system. Thank for using it")
            validate = False
        else:
            print("Invalid option, please choose a number from 1 to 9.")        



 
        

