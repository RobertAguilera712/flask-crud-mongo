import os
from flask import Flask
from flask_pymongo import PyMongo

PASSWORD = os.getenv('MONGO_CRUD_PASSWORD')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bb1131c414ecf54fbcb5ff9253dbff52'
app.config['MONGO_URI'] = f'mongodb+srv://kasparov:{PASSWORD}@cluster0.em4to.mongodb.net/petshop?retryWrites=true&w=majority'
mongo = PyMongo(app)

from crudmongo import routes