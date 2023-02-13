products = [
    {'product_id': 1, 'name': 'Laptop', 'price': 1000},
    {'product_id': 2, 'name': 'Mouse', 'price': 20},
    {'product_id': 3, 'name': 'Keyboard', 'price': 50},
    {'product_id': 4, 'name': 'Monitor', 'price': 200}
]

# Adding a new product
new_product = {'product_id': int(input('Enter ID : ')), 'name': str(input('Enter name product : ')), 'price': int(input('Enter price of product : '))}
products.append(new_product)

print(products)

# Deleting a product
product_to_delete = int(input('Enter id for delete : '))
for product in products:
    if product['product_id'] == product_to_delete:
        products.remove(product)
        break

# Editing a product
product_to_edit = 3
for product in products:
    if product['product_id'] == product_to_edit:
        product['name'] = 'Mechanical Keyboard'
        product['price'] = 80
        break

# Finding a product
product_to_find = 4
for product in products:
    if product['product_id'] == product_to_find:
        found_product = product
        break

print(found_product)
print(products)