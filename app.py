
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
       
    if _name and _email and _password and request.method == "POST":
        _hashed_password = generate_password_hash(_password)
        user = {
            'name': _name,
            'email': _email,
            'pwd': _hashed_password
        }
        mongo.db.users.insert_one(user)
        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp

@app.route('/users/<id>')
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})  # Corrected collection name to lowercase "users"
    resp = dumps(user)
    return resp

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User deleted Successfully")
    resp.status_code = 200
    return resp

# 
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    
    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        

        mongo.db.users.update_one(
            {'_id': ObjectId(_id)},
            {'$set': {'name': _name, 'email': _email, 'pwd': _hashed_password}}
        )
        
        resp = jsonify("User updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'NOT FOUND: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)
