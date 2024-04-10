from flask import Flask,request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    email = db.Column(db.String, nullable=False)
    password= db.Column(db.String, nullable=False)



@app.route('/')
def index():
    new_user = User(email = "test@test.com", password = "123456")
    new_user2 = User(email = "user@user.com", password = "123456")
    
    # db.session.add(new_user)

    # db.session.add(new_user2)

    try:
        db.session.commit()
    except Exception as e:
        print("ERROR:", e)
        db.session.rollback()

    user = User.query.get(4)

    db.session.delete(user)

    try:
        db.session.commit()
    except Exception as e:
        print("ERROR:", e)
        db.session.rollback()

    all_users = User.query.all()

    for user in all_users:
        print("---------------------------------------------------")
        print("USER ID", user.id)
        print("USER EMAIL", user.email)
        print("USER PASSWORD", user.password)
        print("---------------------------------------------------")
    
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug = True, port=5000)
