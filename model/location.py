from flask_restful import fields


location_resource_fields = {
    'type': fields.String(attribute='location_type'),
    'coordinates': fields.List(fields.Float)
}

class Location(object):
    def __init__(self, location_type, coordinates):
        self.location_type = location_type
        self.coordinates = coordinates
