import os
from flask import Flask
import psycopg2
import urlparse


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swaby:620064203@localhost/Contacts'
db = SQLAlchemy(app)


# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["SQLALCHEMY_DATABASE_URI"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

from app import views, models




# from app import db

# class Emails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return '<Emails %r>' % self.name