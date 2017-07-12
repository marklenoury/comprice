from flask_restful import fields
from model.location import location_resource_fields

store_resource_fields_min = {
    '_id':   fields.String,
    'store_type':    fields.String,
    'location_quick_name': fields.String
}


store_resource_fields_all = store_resource_fields_min.copy()
store_resource_fields_all['location'] = fields.Nested(location_resource_fields)


class Store(object):
    def __init__(self, _id, store_type, location_quick_name, location):
        self._id = _id
        self.store_type = store_type
        self.location_quick_name = location_quick_name
        self.location = location
