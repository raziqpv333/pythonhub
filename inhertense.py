class synnefo:
    def python(self):
        print('python')
    def php(self):
        print('php') 
class novavi(synnefo):
    def web_dev(self):
        print('web_dev') 
    def dm(self):
        print('dm')
anu=novavi()
anu.web_dev()
anu.python()   

class synnefo:
    def python(self):
        print('python')
    def php(self):
        print('php') 
class college:
    def ccna(self):
        print("ccna")
class novavi(college,synnefo):
    def web_dev(self):
        print('web_dev') 
    def dm(self):
        print('dm')                
anu=novavi()
anu.web_dev()
anu.python()  
anu.ccna()       

class synnefo:
    def python(self):
        print('python')
    def php(self):
        print('php') 
class novavi(synnefo):
    def web_dev(self):
        print('web_dev') 
    def dm(self):
        print('dm')     
class college(novavi):
    def ccna(self):
        print("ccna")  
sanu=novavi()
sanu.python()
sanu.web_dev()                  

class synnefo:
    def python(self):
        print('python')
    def php(self):
        print('php') 
class novavi(synnefo):
    def web_dev(self):
        print('web_dev') 
    def dm(self):
        print('dm')     
class college(synnefo):
    def ccna(self):
        print("ccna")     
manu=college()
manu.ccna()
sasi=novavi()
sasi.dm()


class A:
    def a1(self):
        print("a1")
class B(A):
    def b1(self):
        print("b1")
class C(A):
    def c1(self):
        print("c1")                
class D(B):
    def d1(self):
        print("d1")
class E(B):
    def e1(self):
        print("e1") 
class F(C):
    def f1(self):
        print("f1")               
fafa=D()
fafa.b1()
joku=E()
joku.a1()
paru=F()
paru.f1()
