"""
from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Registry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(80), unique=True, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Registry %r>' % self.endpoint


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registry = db.Column(db.String(80), unique=True, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
    #     nullable=False)
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Transaction %s>' % self.registry
"""