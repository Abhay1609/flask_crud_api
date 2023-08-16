from flask_restful import Resource
from flask import request, jsonify
from models.user_model import UserModel
from bson.json_util import dumps

class UserResource(Resource):
    def __init__(self, mongo):
        self.model = UserModel(mongo)

    def get(self, user_id):
        user = self.model.get_user(user_id)
        if user:
            return dumps(user)
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        deleted_count = self.model.delete_user(user_id)
        if deleted_count > 0:
            return {'message': 'User deleted successfully'}
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        json_data = request.json
        name = json_data['name']
        email = json_data['email']
        password = json_data['pwd']

        if name and email and password:
            modified_count = self.model.update_user(user_id, name, email, password)
            if modified_count > 0:
                return {'message': 'User updated successfully'}
            return {'message': 'User not found'}, 404
        return {'message': 'Missing data'}, 400

class UsersResource(Resource):
    def __init__(self, mongo):
        self.model = UserModel(mongo)

    def get(self):
        users = self.model.get_all_users()
        return dumps(users)

    def post(self):
        json_data = request.json
        name = json_data['name']
        email = json_data['email']
        password = json_data['pwd']

        if name and email and password:
            self.model.create_user(name, email, password)
            return {'message': 'User added successfully'}
        return {'message': 'Missing data'}, 400
