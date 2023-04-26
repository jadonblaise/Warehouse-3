from data import personnel, stock
from datetime import datetime
from collections import Counter

def get_user_name() -> str:
    username = input('Enter a name: ')
    return username.capitalize()


def greet_user(name):
    print(f"Hello {name}")


def get_selected_operation():
    print(f"What would you like to do? \n1. List items by warehouse \n2. Search an item and place an order "
          f"\n3. Browse by category \n4. Quit")
    choice = int(input('Which operation do you want: '))
    return choice


def list_items_by_warehouse():
    count1 = 0
    count2 = 0
    for item in stock:
        print(f"{item['state'].capitalize()} {item['category'].capitalize()}")
        if item['warehouse'] == 1:
            count1 += 1
        elif item['warehouse'] == 2:
            count2 += 1
    print(f'Total items in warehouse 1: {count1}')
    print(f'Total items in warehouse 2: {count2}')
    print(f"Thank you for your visit, {get_user_name()}!")


def search_and_order_item():
    search = input("what is the name of the Item? ")
    emp_list = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for item in stock:
        match = f"{item['state']} {item['category']}"
        if search.upper() == match.upper():
            #print(item)
            if item['warehouse'] == 1:
                count1 += 1
            elif item['warehouse'] == 2:
                count2 += 1
            elif item['warehouse'] == 3:
                count3 += 1
            elif item['warehouse'] == 4:
                count4 += 1
            emp_list.append(item)
    total_amt = count1 + count2 + count3 + count4
    if total_amt:
        print("Amount available: ", total_amt)
        print("Location:")
        for item in emp_list:
            item_date = datetime.strptime(item['date_of_stock'], '%Y-%m-%d %H:%M:%S')
            day_left = datetime.today() - item_date
            print(f"- Warehouse {item['warehouse']} (in stock for {day_left.days} days)")
        if (count1 >= count2) or (count1 >= count3) or (count1 >= count4):
            print(f"Maximum availability: {count1} in Warehouse 1")
        elif (count2 >= count1) or (count2 >= count3) or (count2 >= count4):
            print(f"Maximum availability: {count2} in Warehouse 2")
        elif (count3 >= count1) or (count3 >= count2) or (count3 >= count4):
            print(f"Maximum availability: {count3} in Warehouse 3")
        elif (count4 >= count1) or (count4 >= count3) or (count4 >= count2):
            print(f"Maximum availability: {count4} in Warehouse 4")
    else:
        print("Location: Not in stock")


    ask = input('Do you want to place an order for this item?(y/n): ')
    order_count = 1
    while ask == 'y':
        if order_count == 1:
            user = input('User login name: ').capitalize()
            check_pass = password_check(personnel, user)
            old_name = user
        else:
            user = input('User login name: ').capitalize()
            if user == old_name:
                pass
            else:
                check_pass = password_check(personnel, user)
                old_name = user
        order_count += 1
        if check_pass == 1:
            num = int(input('How many do you want?: '))
            if num <= total_amt:
                print(f'The order has been placed. Item name {search} and amount ordered {num}')
                break
            elif num > total_amt:
                ans_max = input(f"There are not this many available. The maximum amount that can be ordered "
                                f"is {total_amt}\n Would you like to order the maximum available?(y/n) ")
                if ans_max == 'y':
                    print(f'The order has been placed. Item name {search} and amount ordered {total_amt}')

                else:
                    break

def browse_by_category():
    categories = []
    for item in stock:
        categories.append(item['category'])
    counted = Counter(categories)
    category_list = []
    for index, (category, qty) in enumerate(counted.items()):
        category_list.append(category)
        print(f"{index + 1} {category} ({qty})")
    choice_cat = int(input('\n Type the number of the category to browse: '))
    chosen_cat = category_list[choice_cat - 1]
    print(f'List of {chosen_cat} available: ')
    for i in stock:
        if i['category'] == chosen_cat:
            print(f"{i['state']} {i['category']}, Warehouse{i['warehouse']}")
    print(f"\nThank you for your visit, {get_user_name()}!")


def check_name(personnel, username):
    for item in personnel:
        if item['user_name'] == username:
            return item
        elif 'head_of' in item:
            user = check_name(item['head_of'], username)
            if user:
                return user
    return None


def password_check(personnel, username):
    user = check_name(personnel, username)
    while not user:
        print(f'User {username} not found !!')
        username = input('Enter correct Username: ').capitalize()
        user = check_name(personnel, username)
    password = input('User login password: ')
    if password == user['password']:
        print('Login successful')
        return 1
    else:
        print('Incorrect Password!! Try again')
        return 0




