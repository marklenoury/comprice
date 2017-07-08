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

client = MongoClient('127.0.0.1', 27017)
db = client.comprice
product_types = db.product_types
product_types.insert_many(ProductTypes)

products = db.products
products.insert_many(Products)

store_types = db.store_types
store_types.insert_many(StoreTypes)

stores = db.stores
stores.insert_many(Stores)
