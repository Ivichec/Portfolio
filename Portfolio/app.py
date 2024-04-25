from flask import Flask, render_template
#python app.py --reload
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=False)