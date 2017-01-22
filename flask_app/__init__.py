from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gifdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'secreeeeet_key'
db = SQLAlchemy(app)
db.create_all()

import flask_app.views