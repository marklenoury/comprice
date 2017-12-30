from werkzeug.security import safe_str_cmp
import hashlib
import uuid
from model.user import User

class SecurityControl:
    def __init__(self, user_collection):
        self.user_collection = user_collection

    def authenticate(self, username, password):
        user_bson = self.user_collection.find_one({"_id": username})
        if user_bson:
            salty = password + user_bson['salt']
            hashed = hashlib.sha512(salty.encode('utf-8')).hexDigest()
            if safe_str_cmp(hashed, user_bson['password']):
                return User(user_bson['_id'], user_bson['role'])

    def identity(self, payload):
        user_id = payload['identity']
        user_bson = self.user_collection.find_one({"_id": user_id})
        if user_bson:
            return User(user_bson['_id'], user_bson['role'])

    def create(self, username, password):
        salt = uuid.uuid4().hex
        salty = password + salt
        hashed = hashlib.sha512(salty.encode('utf-8')).hexDigest()
        new_user = {
            '_id': username,
            'salt': salt,
            'role': 'user',
            'password': hashed
        }
        self.user_collection.insert_one(new_user)
