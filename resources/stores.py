from flask import request
from flask_restful import Resource, marshal_with
from flask_jwt import jwt_required
from model.store import Store, store_resource_fields_all
from model.location import Location
import bson

class Stores(Resource):
    def __init__(self, **kwargs):
        self.stores_collection = kwargs['stores_collection']

    @marshal_with(store_resource_fields_all)
    def get(self):
        stores = []
        for store_bson in self.stores_collection.find():
            #TODO refactor out into mapper
            store = Store(str(store_bson['_id']),
                          store_bson['store_type'],
                          store_bson['location_quick_name'],
                          Location(store_bson['location']['type'], store_bson['location']['coordinates']))
            stores.append(store)
        return stores


    #insert
    # TODO input validations, Error handling
    @jwt_required()
    @marshal_with(store_resource_fields_all)
    def post(self):
        data = request.get_json()
        store_bson = self.stores_collection.find_one({
            'store_type': data['store_type'],
            'location.coordinates': data['location']['coordinates']
        })
        if store_bson:
            return {'message': 'item exists'}, 400
        new_store = {
            '_id': bson.ObjectId(),
            'store_type': data['store_type'],
            'location': data['location'],
            'location_quick_name': data['location_quick_name']
        }

        self.stores_collection.insert_one(new_store)
        store = Store(str(new_store['_id']),
                      new_store['store_type'],
                      new_store['location_quick_name'],
                      Location(new_store['location']['type'], new_store['location']['coordinates']))
        return store


