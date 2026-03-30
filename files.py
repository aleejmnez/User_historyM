import csv
#funciont to save inventory to csv file, it takes the inventory list, the path to save and an optional parameter to include header
def save_csv(inventory, path, include_header=True):
    if not inventory:
        print("Cannot save: inventory is empty.")
        return

    try:#try catch error handling for file operations, it handles permission errors, IO errors and unexpected errors
        with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            if include_header:
                writer.writerow(['name','price','quantity'])

            for product in inventory:
                name = product.get('name_product', '').strip()
                price = product.get('price', 0) #if price not found, default to 0
                quantity = product.get('quantity', 0) #if quantity not found, default to 0
                writer.writerow([name, price, quantity])

        print(f"Inventory saved to: {path}") #path is the filename or path where the inventory was saved successfully


    except PermissionError: #Error for not have permission to writte to the file
        print(f"Error: permission denied to write to '{path}'. Check permissions.")
    except IOError as error:
        print(f"I/O error writing file '{path}': {error}") #error for input/output beacuse of disk issues, file system error
    except Exception as error:
        print(f"Unexpected error saving CSV: {error}")#error unexpectd for example dont have space in disk, or other issues


def load_csv(path): #funcion to load the inventory from a csv file
    
    products = [] #list to store the products loaded from the csv file
    invalid_rows = 0 #counter to keep rows invalid
    
    try:
        with open(path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            
            # Validate header
            try:
                header = next(reader)
            except StopIteration:
                print("Error: empty file or missing header.")
                return None
            
            if header != ['name', 'price', 'quantity']:
                print(f"Error: invalid header. Expected: name,price,quantity")
                print(f"Found header: {header}")
                return None
            
            # Process rows
            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 3:
                        print(f"Row {row_number}: invalid column count ({len(row)}, expected 3). Skipped.")
                        invalid_rows += 1
                        continue
                    
                    name, price_str, quantity_str = row
                    name = name.strip()
                    
                    # Validate name
                    if not name:
                        print(f"Row {row_number}: empty name. Skipped.")
                        invalid_rows += 1
                        continue
                    
                    # Convert and validate price
                    try:
                        price = float(price_str)
                    except ValueError:
                        print(f"Row {row_number}: price '{price_str}' is not a valid number. Skipped.")
                        invalid_rows += 1
                        continue
                    
                    if price < 0:
                        print(f"Row {row_number}: negative price (${price}). Skipped.")
                        invalid_rows += 1
                        continue
                    
                    # Convert and validate quantity
                    try:
                        quantity = int(quantity_str)
                    except ValueError:
                        print(f"Row {row_number}: quantity '{quantity_str}' is not a valid integer. Skipped.")
                        invalid_rows += 1
                        continue
                    
                    if quantity < 0:
                        print(f"Row {row_number}: negative quantity ({quantity}). Skipped.")
                        invalid_rows += 1
                        continue
                    
                    # Create valid product
                    product = {
                        'name_product': name,
                        'price': price,
                        'quantity': quantity
                    }
                    products.append(product)
                
                except Exception as error:
                    print(f"Row {row_number}: unexpected error ({error}). Skipped.")
                    invalid_rows += 1
                    continue
        
        # Summary
        print(f"\n===================================================")
        print(f"Load complete: {len(products)} products loaded, {invalid_rows} invalid rows skipped.")
        if invalid_rows > 0:
            print(f"Warning: {invalid_rows} row(s) were skipped due to validation errors.")
        print(f"===================================================\n")
        
        return products
    
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: the file '{path}' is not UTF-8 encoded. Check encoding.")
        return None
    except Exception as error:
        print(f"Unexpected error loading CSV: {error}")
        return None


def ask_load_action(): #function to ask overwrite or merge inventory
   
    action = input("\nOverwrite current inventory? (YES/NO): ").strip().upper()

    if action == 'YES':
        print("Action: Overwrite current inventory.")
        return 'overwrite'

    if action == 'NO':
        print("Action: Merge inventories.")
        return 'merge'

    print("Invalid option. Unrecognized value. Load operation will be cancelled.")
    return None


def overwrite_inventory(current_inventory, new_inventory): #function to overwrrite the current inventory
    
    print("Current inventory overwritten with loaded data.")
    return [product.copy() for product in new_inventory]


def merge_inventory(current_inventory, new_inventory):#function to merge the current inventory with the new inventory
    
    merged_count = 0 #counter to keep track of merged products
    new_count = 0 #counter to keep track of new products

    for new_product in new_inventory: #for each product in the new inventory, 
        new_name = new_product['name_product'].strip().lower()
        found = False

        for current_product in current_inventory: #for each product in the current inventory, if the name matches the new product, merge them by updating the quantity and price
            if current_product['name_product'].strip().lower() == new_name:
                previous_quantity = current_product['quantity']
                previous_price = current_product['price']

                current_product['quantity'] += new_product['quantity']
                current_product['price'] = new_product['price']

                print(f" New product added '{new_product['name_product']}': quantity {previous_quantity} + {new_product['quantity']} = {current_product['quantity']}, price ${previous_price} → ${current_product['price']}")
                merged_count += 1
                found = True
                break

        if not found:
            current_inventory.append(new_product.copy())
            print(f" New: '{new_product['name_product']}' (${new_product['price']}, qty: {new_product['quantity']})")
            new_count += 1

    return current_inventory, merged_count, new_count


merge_inventories = merge_inventory #