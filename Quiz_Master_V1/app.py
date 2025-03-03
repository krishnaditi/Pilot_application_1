# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User, Post
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
# import matplotlib.pyplot as plt
# import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aditi.sqlite'
app.config['SECRET_KEY'] = '1234aditi34'
db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


# Initialize the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
