from flask import Flask, request, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'learnpymongo'
# app.config['MONGO_URI'] = "mongodb+srv://ajayvardhanreddy:ajayvardhan@learnmongo.dba5m.mongodb.net/learnpymongo?retryWrites=true&w=majority"
app.config['MONGO_URI'] =os.environ.get("DATABASE_URL")

mongo = PyMongo(app)

users = mongo.db.mongocol


@app.route('/')
def home():
    return "Hello World"


@app.route('/insert')
def insert():
    users.insert_one({'name':'Dhoni', 'age':40, 'location':'Hyd'})
    return 'Done'


@app.route('/read/<id>')
def read(id):
    user_item = users.find_one({'_id': ObjectId(id)})
    return user_item['name']


@app.route('/delete/<id>')
def delete(id):
    users.delete_one({'_id': ObjectId(id)})
    return 'deleted'


@app.route('/update/<id>')
def update(id):
    # user_item = users.find_one({'_id': ObjectId(id)})
    # user_item['age'] = 21
    users.update_one({'_id': ObjectId(id)}, {"$set": {"age": 21}})
    return "Updated"


if __name__ == "__main__":
    app.run(debug=True)
