def addProduct(product):

    product = {'product_id': int(input('Enter ID : ')), 'name': str(input('Enter name product : ')), 'price': int(input('Enter price of product : '))}
    products.append(product)

def delete_product(product, product_to_delete):
    for i, product in enumerate(products):
        if product['product_id'] == product_id:
            del products[i]
            print("Product deleted successfully!")
            return products