from validate_options import validate_input_product_name, validate_input_price, validate_input_quantity, validate_id,ask_number_postive, validate_input_course
#menu options. 

#function to add product details: name, quantity, and price
def add_name(inventory): 
    id = ask_number_postive()
    
    while not validate_id(id, inventory): #while the name is not unique, it will keep asking for new name. 
        print(f"ERROR: The name '{id}' already exists in the system. Please enter a different name.")
        id = ask_number_postive()

    name=validate_input_product_name()
    Age = validate_input_quantity()
    course = validate_input_course()
    Status = input("Add the status of the students: ")

    students = {
        "Name_students": name, 
        "Id": id,
        "Age": Age,
        "Course": course,
        "Status": Status,
    }    

    inventory.append(students)


def show_students(inventory):
    if not inventory:
        print ("Information empty")
        return
    

    for students in inventory:
        print("-----------------------------------------------------")
        print("---------INFORMATION OF THE STUDENTS ADDED-----------")
        print(f"The name of the students is: {students['Name_students']}")
        print(f"The id of the students is: {students['Id']}")
        print(f"The age of the students is: {students['Age']}")
        print(f"The course of the students is: {students['Course']}")
        print(f"The status of the students is: {students['Status']}")
        print("-----------------------------------------------------")

def search_students(inventory):
    found = False
    if not inventory:
        print("Information empty. Add the information of the students .")
        return

    query = int(input("Enter the id to search: "))#query is key of name product to search in inventory
    if query == "":
        print("Search query cannot be empty.")
        return

   
    for students in inventory:
        if students['Id'] == query:
            found = True
        print("---------SEARCH INFORMATION OF THE STUDENT-----------")
        print(f"The name of the students is: {students['Name_students']}")
        print(f"The id of the students is: {students['Id']}")
        print(f"The age of the students is: {students['Age']}")
        print(f"The course of the students is: {students['Course']}")
        print(f"The status of the students is: {students['Status']}")
        print("-----------------------------------------------------")

    if not found:
        print(f"No information found with id '{query}'.")

def update_students(inventory): 
    found = False
    if not inventory:
        print("Information empty. Add the information of the students .")
        return

    query = int(input("Enter the id to search: "))#query is key of name product to search in inventory
    if query == "":
        print("Search query cannot be empty.")
        return

    for students in inventory:
        if students['Id'] == query: #for used the query to search the product in inventory to update
            found = True
        print("---------SEARCH INFORMATION OF THE STUDENT-----------")
        print(f"The name of the students is: {students['Name_students']}")
        print(f"The id of the students is: {students['Id']}")
        print(f"The age of the students is: {students['Age']}")
        print(f"The course of the students is: {students['Course']}")
        print(f"The status of the students is: {students['Status']}")
        print("-----------------------------------------------------")
            
        print("\nWhat do you want to update?")
        print("1- Name")
        print("2- Age")
        print("3- Course")
        print("4- Status")
            
        option = input("Please choose an option 1-4: ")
            
        if option == "1":
                students['Name'] = validate_input_product_name()
                print("Name updated successfully.")
                
        elif option == "2":
                students['Age'] = validate_input_quantity()
                print("Age updated successfully.")

        elif option == "3":
            students ['Course'] = validate_input_course()
            print("Course updated successfully")

        elif option == "4":
            students ['Status']
            print("Status updated sucessfully")    
                
        else:
                print("Invalid option. try again")
            
        print("----------------UPDATED INFORMATION----------------")
        print(f"Updated Name students: {students['Name_students']}")
        print(f"Update Age: {students['Age']}")
        print(f"Update Course: ")
        print(f"Updated status: {students['Status']}")
        print("---------------------------------------------------")
        return

    if not found:
        print(f"Not found the id '{query}'.")

def delete_students(inventory): #function to delete a product from the inventory
    found = False
    try:

        if not inventory:
            print("Information empty. Add information first.")
            return

        query = int(input("Enter the Id of the product to delete: ")) #query is key of name product to search in inventory to delete
        if query == "":
            print("Product name cannot be empty.")
            return

        for students in inventory:
            if students['Id'] == query:
                found = True
                inventory.remove(students)
                print(f"The information '{query}' deleted successfully.")
                return
    except KeyboardInterrupt:        

        if not found:
            print(f"No found the information '{query}'.")
