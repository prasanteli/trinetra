from flask import Flask, render_template, request ,url_for
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

@app.route("/details_form", methods=["GET","POST"])
def details_form():
    if request.method == "POST":
        name = request.values.get("full-name")
        email = request.values.get("email")
        age = request.values.get("age")
        gender = request.values.get("gender")
        phone = request.values.get("phone")
        print ("\nname",name,"\nemail",email,"\nage",age,"\ngender",gender,"\nphone",phone)

        data = read_json_data()
        # filter this data based on user info and return only those info in below return statement
        return render_template("schemes.html",data = read_json_data())
    return render_template("details_form.html")

# below are useless, ADD IMP ROUTES above 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/terms_conditions")
def terms_conditions():
    return render_template("terms_conditions.html")

@app.route("/header")
def header():
    return render_template("header.html")

@app.route("/schemes")
def schemes():
    data = read_json_data()
    return render_template("schemes.html",data=data)
    
# --------------------------- NEW FLOW (from index page) ----------------------------
@app.route("/index")
def index():
    return render_template("NEW/index.html")
def read_json_data():
    with open('src\static\data\schemes.json', 'r',encoding="utf-8") as f:
        data = f.read()
        data = json.loads(data)
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv=".env")