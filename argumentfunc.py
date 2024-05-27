def sample(name,age):
    print("name",name)
    print("age",age)
sample("manu",26)
sample("akil",28)
sample(29,"akil")

def sample(*arg):
    print(arg)
sample(10,20,30,40,50,46)
sample()
sample(1)
sample(1,22,3)    


def sample(name,age=20):
    print("name",name)
    print("age",age)
sample("manu",26)
sample("akil")

def sample(name,age):
    print("name",name)
    print("age",age) 
sample(age=26,name="asar") 
sample(name="das",age=52)      

def sample(**arg):
    print(arg)
sample(age=25,name="fogg")
sample(name="looter",age=12)    