from flask import jsonify
from flask_restful import Resource
from bson.json_util import dumps

class ProductTypes(Resource):
    def __init__(self, **kwargs):
        self.product_types_collection = kwargs['product_types_collection']

    def get(self):
        product_types = []
        for product_type in self.product_types_collection.find():
            product_types.append(dumps(product_type))
        return jsonify({'product_types': product_types})
