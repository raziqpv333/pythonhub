# import sqlite3
# con=sqlite3.connect("pythonhub/student.db")
# try:
#     con.execute("create table students(roll_no int,subject text,marks int)")
# except:
#     print("table already exixst")

#con.execute("insert into students(roll_no,name,age)values(1,'sasi',25),(2,'appu',33)")
# con.commit()

#name=input("enter your name")
#roll=int(input("enter your ropll number"))
#age=int(input("enter your age"))
#con.execute("insert into students(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()

# NO=int(input("how many number you want"))
# for i in range(NO):
#     name=input("enter your name")
#     roll=int(input("enter your roll number"))
#     age=int(input("enter your age"))
#     con.execute("insert into students(roll_no,name,age)values(?,?,?)",(roll,name,age))
#     con.commit()


#roll=int(input("enter your roll number"))
#data=con.execute("select * from students where roll_no=?",(roll,))
#for i in data:
  #  print(i) 

#roll=int(input("enter your roll number"))
#name=input("enter your name")
#data=con.execute("select * from students where name=? AND roll=?",(name,roll))
#for i in data:
  #  print(i)
#con.execute("update students set name='benoto' where roll_no=23")   
#con.commit()

#name=input("enter your name")
#roll_no=int(input("enter your roll no"))
#con.execute("update students set name=? where roll_no=?",(name,roll_no))
#con.commit()

#con.execute("delete from students where roll_no=19")
#con.commit()


#roll_no=int(input("enter your roll no"))
#con.execute("delete from students where roll_no=?",(roll_no,))
#con.commit()

# data=con.execute("select * from students where name like'b%'")
# for i in data:
#     print(i)

# data=con.execute("select * from students order by age")
# for i in data:
#     print(i)    

# data=con.execute("select * from students order by age desc")
# for i in data:
#     print(i)


# import sqlite3
# con=sqlite3.connect("student.db")
# try:
#     con.execute("create table marksheet(roll_no int,subject text,mark int)")
# except:
#     print("table already exist")

# con.execute("insert into marksheet(roll_no,subject,mark)values(1,'science',80),(23,'maths',80),(14,'english',60)")
# con.commit()    


import sqlite3
con=sqlite3.connect("student.db")

# data=con.execute("select students.roll_no,students.name,students.age,marksheet.subject,marksheet.mark from students cross join marksheet") 
# for i in data:
#     print(i)

s=con.execute("select subject,count(mark) from marksheet")
for i in s:
    print(i)
    