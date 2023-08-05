from flask import Flask, render_template, request 
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about_us")
def about_us():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/header")
def header():
    return render_template("header.html")

@app.route("/verification")
def verification():
    return render_template("verification.html")

@app.route("/schemes")
def schemes():
    with open('src\static\data\schemes.json', 'r',encoding="utf-8") as f:
        data = f.read()
        data = json.loads(data)
        return render_template("schemes.html",data=data)
    
# --------------------------- NEW FLOW (from index page) ----------------------------
@app.route("/index")
def index():
    return render_template("NEW/index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv=".env")