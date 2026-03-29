import csv

def save_csv(inventory, path, include_header=True):
    if not inventory:
        print("Cannot save: inventory is empty.")
        return

    try:
        with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            if include_header:
                writer.writerow(['name','price','quantity'])

            for product in inventory:
                name = product.get('name_product', '').strip()
                price = product.get('price', 0)
                quantity = product.get('quantity', 0)
                writer.writerow([name, price, quantity])

        print(f"Inventory saved to: {path}")

    except PermissionError:
        print(f"Error: permission denied to write to '{path}'. Check permissions.")
    except IOError as error:
        print(f"I/O error writing file '{path}': {error}")
    except Exception as error:
        print(f"Unexpected error saving CSV: {error}")


def load_csv(path):
    """
    Loads a CSV file and returns a list of valid products.
    Validates header, columns, types and skips invalid rows.
    """
    products = []
    invalid_rows = 0
    
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


def ask_load_action():
    """
    Asks the user whether to overwrite or merge inventories.
    Returns 'overwrite' or 'merge'.
    """
    action = input("\nOverwrite current inventory? (Y/N): ").strip().upper()

    if action == 'Y':
        print("Action: Overwrite current inventory.")
        return 'overwrite'

    if action == 'N':
        print("Action: Merge inventories.")
        print("Merge policy: if a product exists, sum quantity and update price.")
        return 'merge'

    print("Invalid option. Unrecognized value. Load operation will be cancelled.")
    return None


def overwrite_inventory(current_inventory, new_inventory):
    """
    Replaces the current inventory with the loaded inventory.
    """
    print("Current inventory overwritten with loaded data.")
    return [product.copy() for product in new_inventory]


def merge_inventory(current_inventory, new_inventory):
    """
    Merges two inventories by product name (case-insensitive).
    Policy: if exists, sum quantity and update price.
    """
    merged_count = 0
    new_count = 0

    for new_product in new_inventory:
        new_name = new_product['name_product'].strip().lower()
        found = False

        for current_product in current_inventory:
            if current_product['name_product'].strip().lower() == new_name:
                previous_quantity = current_product['quantity']
                previous_price = current_product['price']

                current_product['quantity'] += new_product['quantity']
                current_product['price'] = new_product['price']

                print(f"  ✓ '{new_product['name_product']}': quantity {previous_quantity} + {new_product['quantity']} = {current_product['quantity']}, price ${previous_price} → ${current_product['price']}")
                merged_count += 1
                found = True
                break

        if not found:
            current_inventory.append(new_product.copy())
            print(f"  ✓ New: '{new_product['name_product']}' (${new_product['price']}, qty: {new_product['quantity']})")
            new_count += 1

    return current_inventory, merged_count, new_count


# Maintain compatibility with previous names if used elsewhere
merge_inventories = merge_inventory