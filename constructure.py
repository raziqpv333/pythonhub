class sample:
    def __init__(self):
        self.a=10
        self.b=20
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b) 
num=sample()
num.add()    
num.sub()    


class sample:
    def __init__(self,c):
        self.a=10
        self.b=20
        self.c=c
    def add(self):
            print(self.a+self.b+self.c)
    def sub(self):
        print(self.a-self.b-self.c)
num=sample(15) 
num.add()
num.sub()    

class sample:
     def __init__(self,a,b,c,d):
          print(a,b,c,d,)
num=sample(10,20,30,33)

class sample:
     def __init__(self,*arg):
          print(arg)
num=sample(5,15,20,25)    

class win:
     def __init__(self,name,age=26):
          print('name',name)
          print('age',age)
num=win("manu",20)
num=win("anu")          

class lose:
     def __init__(self,name,age):
          print("name",name) 
          print("age",age)
lose(age=26,name="asar") 
lose(name="das",age=52)      

class born:
     def __init__(self,**arg):
          print(arg)
born(age=25,name="fogg")
born(name="looter",age=12)    


