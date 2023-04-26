from methods import get_user_name, get_selected_operation, greet_user, list_items_by_warehouse, search_and_order_item, browse_by_category

# Get the user name
user_name = get_user_name()
greet_user(user_name)

# Get the user selection
operation = get_selected_operation()


# Execute the operation
if operation == 1:
    list_items_by_warehouse()

elif operation == 2:
    search_and_order_item()

elif operation == 3:
    browse_by_category()

elif operation == 4:
    pass

else:
    print("*" * 50)
    print(operation, "is not a valid operation.")
    print("*" * 50)

# Finish
print(f"Thank you for your visit, {user_name}!")