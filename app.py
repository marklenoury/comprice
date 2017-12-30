from flask import Flask, send_from_directory
from flask_restful import Api
from pymongo import MongoClient
from flask_jwt import JWT

from security import SecurityControl
from resources.product_types import ProductTypes
from resources.stores import Stores
from resources.store import Store

app = Flask(__name__)
app.secret_key = "nosecrets"
api = Api(app)

client = MongoClient('127.0.0.1', 27017)
db = client.comprice

securityControl = SecurityControl(db.users)
jwt = JWT(app, securityControl.authenticate, securityControl.identity)  #auth endpoint


#Store and StoreList backend API
api.add_resource(Stores, '/stores', resource_class_kwargs={'stores_collection': db.stores})
api.add_resource(Store, '/stores/<string:store_id>', resource_class_kwargs={'stores_collection': db.stores})

@app.route('/templates/<path:path>')
def index(path):
    return send_from_directory('templates', path)

#api.add_resource(ProductTypes, '/product_types', resource_class_kwargs={'product_types_collection': db.product_types})

app.run(port=5000)
