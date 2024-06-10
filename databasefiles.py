import sqlite3
con=sqlite3.connect("student.db")
try:
    con.execute("create table students(roll_no int,name text,age int)")
except:
    print("table already exixst")

con.execute("insert into students(roll_no,name,age)values(1,'sasi',25),(2,'appu',33)")
con.commit()

name=input("enter your name")
roll=int(input("enter your ropll number"))
age=int(input("enter your age"))
con.execute("insert into students(roll_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()

NO=int(input("how many number you want"))
for i in range(NO):
    name=input("enter your name")
    roll=int(input("enter your roll number"))
    age=int(input("enter your age"))
    con.execute("insert into students(roll_no,name,age)values(?,?,?)",(roll,name,age))
    con.commit()


roll=int(input("enter your roll number"))
data=con.execute("select * from students where roll_no=?",(roll,))
for i in data:
    print(i) 

roll=int(input("enter your roll number"))
name=input("enter your name")
data=con.execute("select * from students where name=? AND roll=?",(name,roll))
for i in data:
    print(i)
