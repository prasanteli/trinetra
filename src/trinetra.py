from flask import Flask, render_template, request ,url_for
from utils import read_json_data, filter_based_on_user
from db_utils import con, check_if_old_user_else_save_user
from user_model import User
import sqlite3  

app = Flask(__name__)

# --------------- User Routes ---------------------->
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about_us")
def about_us():
    return render_template("about.html")

@app.route("/contact")
def contact():
    if request.method == "POST":
        name = request.values.get("full-name")
        email = request.values.get("email")
        message = request.values.get("message")
        print ("\nname",name,"\nemail",email,"\nmessage",message)
        curr_user = User( name, email, message)
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
        print(check_if_old_user_else_save_user(curr_user))
        data = read_json_data()
        data = filter_based_on_user(curr_user,data)
        return render_template("schemes.html",data = read_json_data())
    return render_template("details_form.html")

@app.route("/terms_conditions")
def terms_conditions():
    return render_template("terms_conditions.html")

# --------------- Admin Routes ---------------------->

@app.route("/admin")
def admin():
    return render_template("admin/admin.html")
 
@app.route("/admin/add")  
def add():  
    return render_template("admin/add.html")  
 
@app.route("/admin/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.values.get("full-name")
            email = request.values.get("email")
            age = request.values.get("age")
            gender = request.values.get("gender")
            phone = request.values.get("phone")
            with sqlite3.connect("user.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Users (name, email, age, gender, phone) values (?,?,?,?,?)",(name, email, age, gender, phone))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the user to the list. Either user already exist or information is in wrong format"  
        finally:  
            return render_template("admin/success.html",msg = msg)  
 
@app.route("/admin/view")  
def view():  
    con = sqlite3.connect("user.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Users")  
    rows = cur.fetchall()  
    return render_template("admin/view.html",rows = rows)  
 
 
@app.route("/admin/delete")  
def delete():  
    return render_template("admin/delete.html")  
 
@app.route("/admin/delete_record",methods = ["POST"])  
def deleterecord():  
    phone = request.form["phone"]  
    with sqlite3.connect("user.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Users where phone = ?",phone)  
            msg = "User successfully deleted"  
        except:  
            msg = "Wrong info. This phone no doesnt exist in DB"  
        finally:  
            return render_template("admin/delete_record.html",msg = msg)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,  debug=True, load_dotenv=".env")