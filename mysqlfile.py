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
# cur.execute("insert into student(roll_no,name,age)values(2,'filu',21),(3,'arshavin',26),(4,'mikel',27),(6,'faroo',25),(7,'mohit',27)")
# con.commit()
# cur.execute("select * from student")
# star=cur.fetchall()
# for i in star:
#     print(i)
# con.commit()
# cur.execute("update student set name='filoo' where roll_no=2")
# con.commit()

# cur.execute("delete from student where roll_no=1")
# con.commit()

# roll_no=int(input("enter your rollnumber"))
# name=input("enter your name")
# data=cur.execute("select * from student where name=%s AND roll_no=%s",(name,roll_no))
# for i in data:
#    print(i)

name=input("enter your name")
roll_no=int(input("enter yuor roll number"))
cur.execute("update student set name=%s where roll_no=%s",(name,roll_no))   
con.commit()

roll_no=int(input("enter your roll no"))
cur.execute("delete from student where roll_no=%s",(roll_no,))
con.commit()





