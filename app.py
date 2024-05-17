from flask import Flask, render_template, url_for
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/particles")
def particles():
    return render_template("index1.html")

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
