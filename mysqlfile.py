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
# cur.execute("insert into student(roll_no,name,age)values(1,'jose',20)")    
# con.commit()
# cur.execute("insert into student(roll_no,name,age)values(2,'filu',21),(3,'arshavin',26)")
# con.commit()
# cur.execute("select * from student")
# star=cur.fetchall()
# for i in star:
#     print(i)
# con.commit()
cur.execute("update student set name='filoo' where roll_no=2")
con.commit()

cur.execute("delete from student where roll_no=1")
con.commit()



