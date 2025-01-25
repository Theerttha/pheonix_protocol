from flask import Flask, render_template, url_for, request, redirect,session

from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta, datetime

app = Flask(__name__)
db = SQLAlchemy()
if os.environ.get('RENDER'):  # Running on Render
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config.update(
    SECRET_KEY='Please work',
    SESSION_TYPE='sqlalchemy',
    SESSION_SQLALCHEMY=db,
    SESSION_SQLALCHEMY_TABLE='sessions',
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=5)
)

class main_post(db.Model):
    __tablename__ = 'main_post'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(1000),nullable=False)
    likes=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f'<Userlog {self.id}>'
class comments(db.Model):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(1000),nullable=False)
    post_id=db.Column(db.Integer,nullable=False)
    likes=db.Column(db.Integer,nullable=False)
    time=db.Column(db.Time,nullable=False)
    def __repr__(self):
        return f'<Userlog {self.username}>'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="GET":
        return render_template("index.html")
@app.route('/reporting',methods=['POST','GET'])
def reporting():
    if request.method=="GET":
        return render_template("reporting.html")
@app.route('/gadgets',methods=['POST','GET'])
def gadgets():
    if request.method=="GET":
        return render_template("gadgets.html")
@app.route('/faqs',methods=['POST','GET'])
def faqs():
    if request.method=='GET':
        return render_template("faqs.html")
def init_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
