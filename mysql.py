import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="raziq pv",
    password="raziqpv333",
    database="student"
)
cur=con.cursor()
# cur.execute("create database student")
try:
    cur.execute("create table student(roll_no int,name text,age int)")
except:
    print("table already ready")
cur.execute("insert into student(roll_no,name,age)values(1,'jose',20)")    
con.commit()