from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:8080/flask-blog'
db = SQLAlchemy(app)

class Contacts(db.Model) :
    sno = db.Column(db.Integer,primary_key=True)
    semail = db.Column(db.String(15))
    spassword = db.Column(db.String(8))
    date = db.Column(db.String(12))


@app.route("/")
def home():
    return render_template('/index.html')
    
@app.route("/about")
def about():
    return render_template('/about.html')
    
@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=='POST' :
        email = request.form.get('email')
        password = request.form.get('password')
        entry = Contacts(semail=email,spassword=password,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('/contact.html')
    
@app.route("/post")
def post():
    return render_template('/post.html')

app.run(debug=True) 