def add_product(products, id, name, price):
    products.append({'id': id,'name': name, 'price': price})
    print("Product added successfully!")
    return products

def delete_product(products, id):
    for i, product in enumerate(products):
        if product['name'] == id:
            del products[i]
            print("Product deleted successfully!")
            return products
    print("Product not found.")

def edit_product(products, id, new_id, new_name, new_price):
    for i, product in enumerate(products):
        if product['id'] == id:
            products[i]['id'] = new_id
            products[i]['name'] = new_name
            products[i]['price'] = new_price
            print("Product edited successfully!")
            return products
    print("Product not found.")

def find_product(products, id):
    for product in products:
        if product['id'] == id:
            print("Product found:", product)
            return product
    print("Product not found.")

def display_menu():
    print("\nMenu:")
    print("1. Add a product")
    print("2. Delete a product")
    print("3. Edit a product")
    print("4. Search for a product")
    print("5. Show dictionaries")
    print("6. Quit")
    return int(input("Enter your choice (1-6): "))

products = []

choice = 0
while choice != 6:
    choice = display_menu()
    if choice == 1:
        id = int(input('Enter id: '))
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        products = add_product(products, id, name, price)
    elif choice == 2:
        name = input("Enter product id: ")
        products = delete_product(products, id)
    elif choice == 3:
        name = input("Enter product id to edit: ")
        new_id = input("Enter new product id: ")
        new_name = input("Enter new product name: ")
        new_price = float(input("Enter new product price: "))
        products = edit_product(products, id, new_id, new_name, new_price)
    elif choice == 4:
        id = int(input("Enter product id to search: "))
        find_product(products, id)
    elif choice == 5:
        print(products)
    elif choice == 6:
        print("Goodbye!")