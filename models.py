"""Models for Blogly."""

from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import ForeignKey

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

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(50), nullable=False, unique=True)

    content = db.Column(db.Text, nullable=False, unique=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now, unique=False)

    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class PostTag(db.Model):

    __tablename__ = "posttag"

    post_id = db.Column(db.Integer, ForeignKey('post.id'), primary_key=True, nullable=False)

    tag_id = db.Column(db.Integer, ForeignKey('tag.id'), primary_key=True, nullable=False)


class Tag(db.Model):

    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), nullable=False, unique=True)


def connect_db(app):
    db.app = app
    db.init_app(app)