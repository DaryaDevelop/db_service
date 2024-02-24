from flask import request
from db_service import app, db
from db_service.model.model import Post, User


@app.get("/posts")
def get_all_posts():
    posts = Post.query.all()
    return {
            "posts": [{
                "id": item.id,
                "title": item.title,
                "body": item.body,
                "user_id": item.user_id
            }for item in posts]
    }, 200
    

@app.post("/posts")
def new_posts():
    title = request.json.get("title")
    body = request.json.get("body")
    check_name = Post.query.filter_by(title=title).first()
    if check_name:
        return {
            "status": 2,
            "description": "Title already exist",
            "data": {}
        }, 400
    uuid = request.headers.get("Token")
    uuid = uuid.split(" ")
    user = User.query.filter_by(uuid=uuid[1]).first()
    item = Post(title=title, body=body, user=user)
    db.session.add(item)
    db.session.commit()
    return {
            "posts": {
                "id": item.id,
                "title": item.title,
                "body": item.body
            }
    }, 200
    
    
@app.put("/posts/<int:id>")
def update_posts(id):
    item = Post.query.get(id)
    if not item:
        return {
            "status": 3,
            "description": "Fail",
            "data": {}
        }, 400
    title = request.json.get("title")
    body = request.json.get("body")
    item.title = title if title else item.title
    item.body = body if body else item.body
    db.session.commit()
    return {
            "posts": {
                "id": item.id,
                "title": item.title,
                "body": item.body
            }
        }, 200
    
    
@app.delete("/posts/<int:id>")
def delete_posts(id):
    item = Post.query.get(id)
    if not item:
        return {
            "status": 3,
            "description": "Fail",
            "data": {}
        }, 400
    db.session.delete(item)
    db.session.commit()
    return {
            "posts": {
                "id": item.id,
                "title": item.title,
                "body": item.body
            }
        }, 200
