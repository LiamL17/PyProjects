
from flask import Flask, render_template

web = Flask(__name__)

@web.route('/')
def home():
    return render_template("home.html")

@web.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    web.run(debug=True)