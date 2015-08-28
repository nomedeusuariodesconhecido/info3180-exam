import os
from flask import Flask


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swaby:620064203@localhost/Contacts'
db = SQLAlchemy(app)


from app import views, models