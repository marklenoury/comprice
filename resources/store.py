from flask_restful import Resource, marshal_with
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

    #delete
