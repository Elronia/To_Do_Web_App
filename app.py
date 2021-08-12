from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/todo'
else:
    app.debug = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#table
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods = ['POST'] )
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(username, email, password)          
        
        # Save it to database
        if db.session.query(Users).filter(Users.username == username).count() == 0:
            data = Users(username,email,password)
            db.session.add(data)
            db.session.commit()
            return render_template('todo.html')

@app.route('/home', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_email = request.form['username_email']
        password = request.form['password']
        # print(username_email,password)

        # if user exists
        user = db.session.query(Users).filter(Users.username == username_email or Users.email == username_email)
        if user.count() != 0:
            pwd = user.first().password
            email = user.first().email
            if(pwd == password or email == username_email):
                return render_template('todo.html')           
    
    return render_template('login.html', message = "Username and Password did not match.")

@app.route('/login')
def logout():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()