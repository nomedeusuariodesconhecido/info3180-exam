from flask import Flask
from app import app
from app import db

@app.before_first_request
def createDB():
    db.create_all()
    db.session.commit()