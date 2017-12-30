from pymongo import MongoClient
import bson
from datetime import datetime

ProductTypes = [
    {
        '_id': 'Bread'
    }
]

Products = [
    {
        '_id': bson.Int64(1),
        'name': 'Superior White Sliced',
        'company': 'Albany Bakeries',
        'barcode': '6001253010178',
        'size': '700g',
        'product_type': 'Bread'
    },

    {
        '_id': bson.Int64(2),
        'name': 'Superior Brown Sliced',
        'company': 'Albany Bakeries',
        'barcode': '6001253010185',
        'size': '700g',
        'product_type': 'Bread'
    },

    {
        '_id': bson.Int64(3),
        'name': 'Superior Best of Both Sliced',
        'company': 'Albany Bakeries',
        'barcode': '6001253010307',
        'size': '700g',
        'product_type': 'Bread'
    },

    {
        '_id': bson.Int64(4),
        'name': 'Superior Wholewheat Sliced',
        'company': 'Albany Bakeries',
        'barcode': '6009518601505',
        'size': '800g',
        'product_type': 'Bread'
    }
]

StoreTypes = [
    {
        '_id': 'Checkers'
    },

    {
        '_id': 'Spar'
    },

    {
        '_id': 'Pick \'n Pay'
    },

    {
        '_id': 'Woolworths'
    }
]

Stores = [
    {
        '_id': bson.ObjectId(),
        'store_type': 'Checkers',
        'location': {
            'type': 'Point',
            'coordinates': [-26.021174, 28.014425]
        },
        'location_quick_name': 'Pineslopes'
    },

    {
        '_id': bson.ObjectId(),
        'store_type': 'Spar',
        'location': {
            'type': 'Point',
            'coordinates': [-26.001026, 27.982547]
        },
        'location_quick_name': 'Broadacres'
    },

    {
        '_id': bson.ObjectId(),
        'store_type': 'Pick \'n Pay',
        'location': {
            'type': 'Point',
            'coordinates': [-26.016848, 27.998928]
        },
        'location_quick_name': 'Cedar Square'
    }
]

MostLikelyCurrentPrice = [
    {
        'product_id': bson.Int64(1),
        'price': 12.95,
        'store_id': bson.ObjectId(Stores[0]['_id']),
    }
]

PriceEvents = [
    {
        'product_id': bson.Int64(1),
        'price': 12.95,
        'store_id': bson.ObjectId(Stores[0]['_id']),
        'date': datetime.utcnow(),
        'captured_by': 'manual'
    }
]

PriceModifiers = [
    {
        'product_id': bson.Int64(1),
        'price': '5.00',
        'store_id': bson.ObjectId(Stores[0]['_id']),
        'from_date': datetime.utcnow(),
        'to_date': datetime.utcnow()
    }
]

Users = [
    {
        '_id': 'nicola.webb',
        'salt': '59850c0fbd2148e5ae80fe8618773600',
        'role': 'superadmin',
        'password': '7104a3d4f75dc34a77515cd09b5f0870ee091272ffaaece55da1768da89cff246c8c2998013e7e2c344398b8c5c2ecba8050195b2cab9e41222cd6161044c27f'
    },

    {
        '_id': 'mark.lenoury',
        'salt': 'a730ad1f7945450782f918132fca08bc',
        'role': 'superadmin',
        'password': '69246c9dcba9b40a0e62fbfabaa62c745d93b7354126a0d0120996db020b0aa58bb7d3ac83513eabc69c4013924ebf4c3aadb6f7f901a16ee5a6a4c5c442ed20'
    }
]

client = MongoClient('127.0.0.1', 27017)
db = client.comprice

users = db.users
users.insert_many(Users)

product_types = db.product_types
product_types.insert_many(ProductTypes)

products = db.products
products.insert_many(Products)

store_types = db.store_types
store_types.insert_many(StoreTypes)

stores = db.stores
stores.insert_many(Stores)
