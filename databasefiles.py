import sqlite3
con=sqlite3.connect("student.db")
try:
    con.execute("create table students(roll_no int,name text,age int)")
except:
    print("table already exixst")

con.execute("insert into students(roll_no,name,age)values(1,'sasi',25),(2,'appu',33)")
con.commit()