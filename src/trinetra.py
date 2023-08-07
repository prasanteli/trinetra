from flask import Flask, render_template, request ,url_for
from utils import read_json_data, filter_based_on_user
from db_utils import con
from user_model import User

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
        curr_user = User( name, email, age, gender, phone)
        check_if_old_user_else_save_user(curr_user)
        data = read_json_data()
        data = filter_based_on_user(curr_user,data)
        return render_template("schemes.html",data = read_json_data())
    return render_template("details_form.html")

@app.route("/terms_conditions")
def terms_conditions():
    return render_template("terms_conditions.html")

@app.route("/schemes")
def schemes():
    data = read_json_data()
    return render_template("schemes.html",data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv=".env")