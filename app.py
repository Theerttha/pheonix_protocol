from flask import Flask, render_template, url_for, request, redirect,session
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def func():
    return "1"
if __name__ == "__main__":
    app.run(debug=True)
