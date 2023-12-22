import sqlalchemy as sa
from db_service import db

class Posts (db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    body = sa.Column(sa.Text, nullable=False)
