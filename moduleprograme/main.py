import add
import sub as m
from mul import mul
import div
import mod

while True:
    print("1.add,2.sub,3.mul,4.div,5.mod,6.exit") 
    choice=int(input("enter a choice number")) 
    if choice==1:
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        add.add(a,b)
    elif choice==2:
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        m.sub(a,b)
    elif choice==3:
        a=int(input("enter a number"))
        b=int(input("enter a number"))    
        mul(a,b)
    elif choice==4:
        a=int(input("enter a number"))
        b=int(input("enter a number"))    
        div.div(a,b)
    elif choice==5:
        a=int(input("enter a number"))
        b=int(input("enter a number"))         
        mod.mod(a,b)
    elif choice==6:
        break
    else:
        print("invalid choice")