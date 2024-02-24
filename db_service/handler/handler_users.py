from flask import request
from db_service import app, db
from db_service.model.model import User


@app.get("/user/<login>")
def sign_up(login):
    is_exist = User.query.filter_by(login=login).first()
    if is_exist:
        return {
            "status": 2,
            "description": "User already exist",
            "data": {}
        }, 400
    return {
        "status": 0,
        "description": "OK",
        "data": {}
    }, 200


@app.post("/user")
def registration():
    login = request.json.get("login")
    password = request.json.get("password")
    new_user = User(login=login, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "user": {
                "id": new_user.id,
                "login": new_user.login
            }
        }
    }, 200


@app.post("/sign_in")
def sign_in():
    login = request.json.get("login")
    password = request.json.get("password")
    user = User.query.filter_by(login=login).first()
    if not user or user.password != password:
        return {
            "status": 4,
            "description": "Login or password not match",
            "data": {}
        }, 400
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "user": {
                "uuid": user.uuid,
                "login": user.login
            }
        }
    }, 200


@app.put("/change_password/<login>")
def change_password(login):
    password = request.json.get("password")
    user = User.query.filter_by(login=login).first()
    if not user or user.password != password:
        return {
            "status": 4,
            "description": "Login or password not match",
            "data": {}
        }, 400
    password_new = request.json.get("password_new")
    user.password = password_new
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "user": {
                "id": user.id,
                "login": user.login
            }
        }
    }, 200


@app.delete("/delete_user/<id>")
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return {
            "status": 6,
            "description": "User not found",
            "data": {}
        }, 400
    db.session.delete(user)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "user": {
                "id": user.id,
                "login": user.login
            }
        }
    }, 200
