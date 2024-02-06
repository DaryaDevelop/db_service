import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_CONFIGURATION")
db = SQLAlchemy(app)
migrate = Migrate (app,db)

from db_service.model import model

with app.app_context():
    db.create_all()

from db_service.handler import handler_posts
from db_service.handler import handler_users
