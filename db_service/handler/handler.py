from db_service import app
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
    