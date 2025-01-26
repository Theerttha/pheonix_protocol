from flask import Flask, render_template, url_for, request, redirect,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os,time
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
        return f'<main_post {self.id}>'
class Comments(db.Model):
    __tablename__ = 'commentbox'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(1000),nullable=False)
    post_id=db.Column(db.Integer,nullable=False)
    likes=db.Column(db.Integer,nullable=False)
    time=db.Column(db.Time,nullable=False)
    def __repr__(self):
        return f'<Comments {self.id}>'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="GET":
        session['start']=[]
        session['comment']=[]
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
@app.route('/pheonix',methods=['POST','GET'])
def community():
    comments=Comments.query.order_by(Comments.time).all()
    d={}
    for i in comments:
        if i.post_id not in d:
            d[i.post_id]=[i.content]
        else:
            d[i.post_id].append(i.content)

    if request.method=='GET':
        stories=main_post.query.order_by(desc(main_post.likes)).all()
        return render_template("pheonix.html",stories=stories,d=d,comment=session['comment'])
    if request.method=='POST':
        post_like=request.form.get('post_like')

        #post_comment=request.form['']
        #comment_val=request.form['']
        
        if post_like!=None:
            stories=main_post.query.order_by(desc(main_post.likes)).all()
            x=int(post_like)
            for i in stories:
                if i.id==x:
                    if i.id not in session['start']:
                        try:
                            likes=session['start']
                            likes.append(i.id)
                            session.pop('start')
                            session['start']=likes
                            i.likes+=1
                            db.session.commit()
                            return redirect(url_for('community'))
                        except:
                            return "error"
                    else:
                        return redirect(url_for('community'))

                
            return redirect(url_for('community'))
        post_content = request.form.get('pheonix_story')
        post_submit= request.form.get('submit_story')
        if post_submit!=None:
            new_line = main_post(content=post_content, likes=0)
            try:

                db.session.add(new_line)
                db.session.commit()
                return redirect(url_for('community'))
            except Exception as e:
                db.session.rollback()
                return "error"
        comment_button=request.form.get('comment_button')

        if comment_button!=None:
            comment_button=int(comment_button)
            if comment_button not in session['comment']:
                session['comment_button']=comment_button
                c=session['comment']
                c.append(comment_button)
                session.pop('comment')
                session['comment']=c
             
                return redirect(url_for('community'))
            else:
                c=session['comment']
                c.remove(comment_button)
                session.pop('comment')
                session['comment']=c
              
                
                return redirect(url_for('community'))
        comment_pheonix=request.form.get('comment_pheonix')
        comment_submit=request.form.get('comment_submit')
        if comment_pheonix!=None:
            new_line=Comments(content=comment_pheonix,post_id=session['comment_button'],likes=0,time=datetime.now())
           
            try:
                db.session.add(new_line)
                db.session.commit()
                return redirect(url_for('community'))
            except Exception as e:
                db.session.rollback()
                return "error"

        return redirect(url_for('community'))
def init_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
