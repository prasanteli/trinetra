from flask import Flask, render_template, request 
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about_us")
def about_us():
    return render_template("about.html")

@app.route("/scheme")
def scheme():
    with open('src\static\data\schemes.json', 'r',encoding="utf-8") as f:
        data = f.read()
        data = json.loads(data)
        return render_template("scheme.html",data=data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv=".env")