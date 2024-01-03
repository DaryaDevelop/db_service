import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_CONFIGURATION")
db = SQLAlchemy(app)

from db_service.model import model

with app.app_context():
    db.create_all()

from db_service.handler import handler
