# Write a python code to build Ajax enabled web application for product

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dummy product data (in real application, use a database)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 20.49},
    {'id': 3, 'name': 'Product 3', 'price': 15.99}
]

@app.route('/')
def index():
    return render_template('index.html')

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

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
    return jsonify(new_product), 201

# Route to delete a product by its ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [item for item in products if item['id'] != product_id]
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)


"""
html code

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajax Product Management</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function(){
            // Function to load products from server
            function loadProducts(){
                $.get('/products', function(data){
                    $('#product-list').empty();
                    $.each(data, function(index, product){
                        $('#product-list').append(`<li>${product.name} - ${product.price} <button class="delete-btn" data-id="${product.id}">Delete</button></li>`);
                    });
                });
            }

            // Load products on page load
            loadProducts();

            // Handle form submission to add product
            $('#add-product-form').submit(function(event){
                event.preventDefault();
                var name = $('#name').val();
                var price = $('#price').val();
                $.post('/products', JSON.stringify({name: name, price: price}), function(data){
                    loadProducts();
                    $('#name').val('');
                    $('#price').val('');
                });
            });

            // Handle click event on delete button
            $(document).on('click', '.delete-btn', function(){
                var productId = $(this).data('id');
                $.ajax({
                    url: '/products/' + productId,
                    type: 'DELETE',
                    success: function(){
                        loadProducts();
                    }
                });
            });
        });
    </script>
</head>
<body>
    <h1>Ajax Product Management</h1>
    <form id="add-product-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" required>
        <button type="submit">Add Product</button>
    </form>
    <ul id="product-list"></ul>
</body>
</html>


"""