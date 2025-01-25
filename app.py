from flask import Flask, render_template, url_for, request, redirect,session
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="GET":
        return render_template("index.html")
@app.route('/gadgets',methods=['POST','GET'])
def gadgets():
    if request.method=="GET":
        return render_template("gadgets.html")
if __name__ == "__main__":
    app.run(debug=True)
