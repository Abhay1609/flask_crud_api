
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
# from app.controllers.user_controller import UserResource, UsersResource
from controllers.user_controller import UserResource, UsersResource

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb+srv://abhaypratap9848:abhaypratap9848@cluster0.6zvqwxd.mongodb.net/Users?retryWrites=true&w=majority"
mongo = PyMongo(app)
api = Api(app)

api.add_resource(UserResource, '/users/<string:user_id>', resource_class_kwargs={'mongo': mongo})
api.add_resource(UsersResource, '/users', resource_class_kwargs={'mongo': mongo})

if __name__ == "__main__":
    app.run(debug=True)

