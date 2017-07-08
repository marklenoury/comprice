from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

from resources.product_types import ProductTypes
from resources.stores import Stores

app = Flask(__name__)
api = Api(app)

client = MongoClient('127.0.0.1', 27017)
db = client.comprice

# class Stores(Resource):
#     def get(self):
#         stores = db.stores
#         store_ret = []
#         for store in stores.find():
#             store_ret.append(dumps(store))
#         return jsonify({'stores': store_ret})





api.add_resource(Stores, '/stores', resource_class_kwargs = {'stores_collection': db.stores})
api.add_resource(ProductTypes, '/product_types', resource_class_kwargs = {'product_types_collection': db.product_types})

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index.html')
#
# @app.route('/store', methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
#
# @app.route('/store/<string:name>', methods=['GET'])
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#     return jsonify({'message': 'store not found'})
#
# @app.route('/store', methods=['GET'])
# def get_stores():
#     return jsonify({'stores': stores})
#
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_store_item(name):
#     for store in stores:
#         if store['name'] == name:
#             request_data = request.get_json()
#             item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].append(item)
#             return jsonify(item)
#     return jsonify({'message': 'store not found'})
#
# @app.route('/store/<string:name>/item', methods=['GET'])
# def get_store_items(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items': store['items']})
#     return jsonify({'message': 'store not found'})


app.run(port=5000)
