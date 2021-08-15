from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Easy12345!@localhost:5432/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Models of Tables
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # print(username, email, password)

        # Save it to the database
        if db.session.query(Users).filter(Users.username == username or Users.email == email).count() == 0:
            data = Users(username, email, password)
            db.session.add(data)
            db.session.commit()
            print('saved successfully')

    return render_template('todo.html')

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username_email = request.form['username_email']
        password = request.form['password']

        #check the user account
        user = db.session.query(Users).filter(Users.username == username_email or Users.email == username_email)
        if user.count() != 0:
            pwd = user.first().password
            email = user.first().email
            username = user.first().username
            if(pwd == password or email == username_email or username == username_email):
                return render_template('todo.html')

        return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()