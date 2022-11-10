from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))

    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")


@app.route('/user/signup/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add( User( username=request.form['username'], password=request.form['password'],email=request.form['email'] ) )
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/user/signin/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        e = request.form['email']
        data = User.query.filter_by(username=u, password=p,email=e).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()


if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    app.run()
