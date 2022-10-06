"""Models for Blogly."""

from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False, unique=False)

    last_name = db.Column(db.String(50), nullable=False, unique=False)

    img_url = db.Column(db.Text, nullable=True)

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(50), nullible=False, unique=True)

    content = db.Column(db.Text, nullible=False, unique=False)

    created_at = db.Column(db.DateTime, nullible=False, default=datetime.datetime.now,unique=False)

    user = db.relationship('User')


def connect_db(app):
    db.app = app
    db.init_app(app)