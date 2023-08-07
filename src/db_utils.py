import sqlite3  
con = sqlite3.connect("user.db")  
print("Database opened successfully")  
con.execute(""" drop table if exists Users """)
con.execute("""
            create table Users (
            id INTEGER , 
            name TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL,
            age INTEGER 
            gender TEXT NOT NULL,
            phone INTEGER PRIMARY KEY)
            """)  
  
print("Table created successfully")  


def check_if_old_user_else_save_user(user):
    pass

# con.close()  