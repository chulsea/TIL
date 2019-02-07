from flask import Flask, render_template, request as req, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 기본값은 True, True일 경우 sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등 추적 (과도한 메모리 사용)

# db = SQLAlchemy(app)
db.init_app(app) # 분리시 다음과 같이 초기화
migrate = Migrate(app, db)

@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/users/<int:id>")
def get_user_details(id):
    user = User.query.get(id)
    return render_template("user.html", user=user)

@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if req.method == "GET":
        return render_template("create_user.html")
    user = User(username=req.form["username"], email=req.form["email"])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("get_user_details", id=user.id))

@app.route("/users/update/<int:id>")
def update_user_page(id):
    user = User.query.get(id)
    return render_template("modify_user.html", user=user)

@app.route("/users/update/", methods=["POST"])
def update_user():
    user = User.query.get(req.form["userid"])
    user.username = req.form["username"]
    user.email = req.form["email"]
    db.session.commit()
    return redirect(url_for("get_user_details", id=user.id))

@app.route("/users/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("index"))
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)