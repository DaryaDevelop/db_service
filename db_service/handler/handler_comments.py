from flask import request

from db_service import app, db
from db_service.model.model import Comment, Post, User


@app.get("/comments/<int:id>")
def get_comments(id):
    comments = Comment.query.filter_by(post_id=id).all()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "comment": [{
                "id": item.id,
                "body": item.body,
                "post_id": item.post_id,
                "user_id": item.user_id
            }for item in comments]
        }
    }, 200


@app.post("/comments/<int:id>")
def new_comment(id):
    body = request.json.get("body")
    uuid = request.headers.get("Token")
    uuid = uuid.split(" ")
    user = User.query.filter_by(uuid=uuid[1]).first()
    post = Post.query.filter_by(id=id).first()
    item = Comment(body=body, user=user, post=post)
    db.session.add(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "comment": {
                "id": item.id,
                "body": item.body,
                "post_id": item.post_id,
                "user_id": item.user_id
            }
        }
    }, 200


@app.put("/comments/<int:id>")
def update_comment(id):
    item = Comment.query.get(id)
    if not item:
        return {
            "status": 3,
            "description": "Fail",
            "data": {}
        }, 400
    body = request.json.get("body")
    item.body = body if body else item.body
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "comment": {
                "id": item.id,
                "body": item.body,
                "post_id": item.post_id,
                "user_id": item.user_id
            }
        }
    }, 200


@app.delete("/comments/<int:id>")
def delete_comment(id):
    item = Comment.query.get(id)
    if not item:
        return {
            "status": 3,
            "description": "Fail",
            "data": {}
        }, 400
    db.session.delete(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "comment": {
                "id": item.id,
                "body": item.body,
                "post_id": item.post_id,
                "user_id": item.user_id
            }
        }
    }, 200
