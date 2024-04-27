#Write a python code to build Rest API for product


from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy product data (in real application, use a database)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 20.49},
    {'id': 3, 'name': 'Product 3', 'price': 15.99}
]

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a single product by its ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(new_product)
    return jsonify({'message': 'Product added', 'product': new_product}), 201

# Route to update a product by its ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        data = request.get_json()
        product.update(data)
        return jsonify({'message': 'Product updated', 'product': product})
    return jsonify({'message': 'Product not found'}), 404

# Route to delete a product by its ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [item for item in products if item['id'] != product_id]
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)
