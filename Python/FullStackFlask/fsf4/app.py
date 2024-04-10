from flask import Flask,request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable= False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default= db.func.now())



@app.route('/')
def index():
    all_users = User.query.all() #[<User>,<User>]

    return render_template("home.html", all_users = all_users)

@app.route('/display-add-user')
def displayAddUser():
    return render_template("adduser.html")

@app.route('/adduser', methods = ['GET','POST'])
def adduser():
    new_user = User(name = request.form['name'], email = request.form['email'])

    db.session.add(new_user)

    try:
        db.session.commit()
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()
    
    return redirect('/')

@app.route('/show/<id>')
def show(id):
    user = User.query.get(id)

    return render_template("showuser.html", user=user)

@app.route('/edit/<id>')
def edit(id):
    return render_template("edituser.html", id = id)

@app.route('/edituser/<id>', methods = ['POST','GET'])
def edituser(id):
    user = User.query.get(id)
    
    user.name = request.form['name']

    user.email = request.form['email']

    try:
        db.session.commit()
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

    return redirect('/')

@app.route('/delete/<id>')
def deleteuser(id):
    user = User.query.get(id)

    db.session.delete(user)

    try:
        db.session.commit()
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug = True, port=5000)
