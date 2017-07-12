from flask_restful import Resource, marshal_with
from model.store import Store, store_resource_fields_all
from model.location import Location

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
