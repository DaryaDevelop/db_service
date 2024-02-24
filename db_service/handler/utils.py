from db_service import app, db
from db_service.model.model import Post, User

@app.get("/is_owner/<int:id>")
def is_owner(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        return {
            "status": 3,
            "description": "Fail",
            "data": {}
        }, 400
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "user_id": {
                "uuid": post.user.uuid
            }
        }
    }, 200

@app.get("/check_login/<uuid>")
def check_login(uuid):
    user = User.query.filter_by(uuid=uuid).first()
    if not user:
        return {
            "status": 6,
            "description": "User not found",
            "data": {}
        }, 400
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "uuid": user.uuid
        }
    }, 200
