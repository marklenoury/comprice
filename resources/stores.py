from flask import jsonify
from flask_restful import Resource
from bson.json_util import dumps

class Stores(Resource):
    def __init__(self, **kwargs):
        self.stores_collection = kwargs['stores_collection']

    def get(self):
        stores = []
        for store in self.stores_collection.find():
            stores.append(dumps(store))
        return jsonify({'stores': stores})