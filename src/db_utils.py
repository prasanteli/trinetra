import sqlite3  
con = sqlite3.connect("user.db")  
print("Database opened successfully")  
con.execute(""" drop table if exists Users """)
con.execute("""
            create table Users (
            id INTEGER , 
            name TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone INTEGER PRIMARY KEY)
            """)  
  
print("Table created successfully")  


def check_if_old_user_else_save_user(user):
    con = sqlite3.connect("user.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Users")  
    rows = cur.fetchall()  
    if user not in rows :
        with sqlite3.connect("user.db") as con:  
                    cur = con.cursor()  
                    cur.execute("INSERT into Users (name, email, age, gender, phone) values (?,?,?,?,?)",(user.name, user.email, user.age, user.gender, user.phone))  
                    con.commit()  
        return "User created"
    return "User already present"

# con.close()  