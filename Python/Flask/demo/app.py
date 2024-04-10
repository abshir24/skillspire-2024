from flask import Flask,request, render_template,redirect,session

app = Flask(__name__)

app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formdata',methods = ['GET','POST'])
def formdata():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']

    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5000)