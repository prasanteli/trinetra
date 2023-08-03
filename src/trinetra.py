from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about_us")
def about_us():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv="./.flaskenv")