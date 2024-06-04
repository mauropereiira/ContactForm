from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#creating db file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
#not tracking all modifications on db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

