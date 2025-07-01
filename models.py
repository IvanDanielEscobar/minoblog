from datetime import datetime, timezone

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    mail = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    post = db.relationship(
        'Post',
        backref='author',
        lazy=True
    )

    comments = db.relationship(
        'Comment', 
        backref='author', 
        lazy=True
        )

    def __str__(self):
        return self.name 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(2500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return self.title
    

    
#tabla de asociacion entre post y category
post_category = db.Table(
    'post_category',
    db.column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(2000), nullable=False)
    date_create = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __str__(self):
        return f"Comment {self.id} on '{self.post.title}' by {self.author.username}"
    
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __str__(self):
        return self.name