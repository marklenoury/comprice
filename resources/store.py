from flask import request
from flask_restful import Resource, marshal_with
from flask_jwt import jwt_required
from model.store import Store as StoreModel, store_resource_fields_all
from model.location import Location
import bson

class Store(Resource):
    def __init__(self, **kwargs):
        self.stores_collection = kwargs['stores_collection']

    @marshal_with(store_resource_fields_all)
    def get(self, store_id):
        store_bson = self.stores_collection.find_one({"_id": bson.ObjectId(store_id)})
        store = StoreModel(str(store_bson['_id']),
                      store_bson['store_type'],
                      store_bson['location_quick_name'],
                      Location(store_bson['location']['type'], store_bson['location']['coordinates']))
        return store



    #update
    @jwt_required()
    @marshal_with(store_resource_fields_all)
    def put(self, store_id):
        data = request.get_json()
        store_bson = self.stores_collection.find_one({'_id': bson.ObjectId(store_id)})
        store_bson['location_quick_name'] = data['location_quick_name']
        store_bson['location']['coordinates'] = data['location']['coordinates']
        self.stores_collection.update_one(store_bson)
        store = StoreModel(str(store_bson['_id']),
                           store_bson['store_type'],
                           store_bson['location_quick_name'],
                           Location(store_bson['location']['type'], store_bson['location']['coordinates']))
        return store


    #delete
    @jwt_required()
    def delete(self, store_id):
        self.stores_collection.delete_one({'_id': store_id})
        return '', 204

