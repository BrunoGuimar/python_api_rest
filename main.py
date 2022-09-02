from flask import Flask, request
from datetime import date

app = Flask(__name__)

data_db = dict()


@app.route('/products')
def get_products():
    return data_db, 200

@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    ids = list(data_db.keys())
    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1
    data_db[new_id] = {
        'name': name, 
        'price': price,
        'dated_at': date.today(),
        'id': new_id,
        'type': 'bought',
    }
    return data_db, 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    product = data_db.get(product_id)
    if product:
        name = request.json['name']
        price = request.json['price']
        product['name'] = name
        product['price'] = price
        
        return product, 202
    else:
        return {'Message': "Product not found"}, 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    product = data_db.get(product_id)
    if product:
        del data_db[product['id']]
        return {'Deleted:': product}, 200
    else:
        return {'message': 'Product not found'}, 404

if __name__ == '__main__':
    app.run()