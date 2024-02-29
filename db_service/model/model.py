import uuid

import sqlalchemy as sa

from db_service import db


class Post(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, unique=True, nullable=False)
    body = sa.Column(sa.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post')


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.Text, unique=True, nullable=False)
    password = sa.Column(sa.Text, nullable=False)
    uuid = sa.Column(sa.Uuid, unique=True, nullable=False, default=uuid.uuid4)
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')


class Comment(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
