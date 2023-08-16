from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId

class UserModel:
    def __init__(self, mongo):
        self.mongo = mongo

    def get_user(self, user_id):
        return self.mongo.db.users.find_one({'_id': ObjectId(user_id)})

    def delete_user(self, user_id):
        result = self.mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count

    def update_user(self, user_id, name, email, password):
        hashed_password = generate_password_hash(password)
        result = self.mongo.db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': {'name': name, 'email': email, 'pwd': hashed_password}}
        )
        return result.modified_count

    def get_all_users(self):
        return self.mongo.db.users.find()

    def create_user(self, name, email, password):
        hashed_password = generate_password_hash(password)
        user = {
            'name': name,
            'email': email,
            'pwd': hashed_password
        }
        self.mongo.db.users.insert_one(user)
