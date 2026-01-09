from flask import Flask, request, jsonify, render_template
from models import db, User, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rdbms.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id})

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    user.name = request.json["name"]
    db.session.commit()
    return jsonify({"status": "updated"})

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"status": "deleted"})

@app.route("/users/<int:id>/posts")
def user_posts(id):
    posts = db.session.query(Post).join(User).filter(User.id == id).all()
    return jsonify([
        {"title": p.title, "content": p.content}
        for p in posts
    ])
    
@app.route("/repl", methods=["POST"])
def sql_repl():
    sql = request.json["query"]
    try:
        result = db.session.execute(sql)
        rows = [dict(row) for row in result]
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})
