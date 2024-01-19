from flask import request
from db_service import app, db
from db_service.model.model import Posts


@app.get("/all_posts")
def get_all_posts():
    posts = Posts.query.all()
    return {
            "posts": [{
                "id": item.id,
                "title": item.title,
                "body": item.body
            }for item in posts]
    }, 200
    

@app.post("/new_posts")
def new_posts():
    title = request.json.get("title")
    body = request.json.get("body")
    check_name = Posts.query.filter_by(title=title).first()
    if check_name:
        return {
            "status": 2,
            "description": "Title already exist",
            "data": {}
            }, 400
    item = Posts(title=title, body=body)
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
    item = Posts.query.get(id)
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
    
    
@app.delete("/delete_posts/<int:id>")
def delete_posts(id):
    item = Posts.query.get(id)
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
