from flask import Flask
from sqlalchemy import Column, Integer, String
from . import db

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frst_name = db.Column(db.String(80), unique=True)
    lst_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, frst_name, lst_name, email):
        self.frst_name = frst_name
        self.lst_name = lst_name
        self.email = email

    def __repr__(self):
        return '<Emails %r>' % self.frst_name



