while True:
    NO1=int(input("enter a number"))
    NO2=int(input("enter a number"))
    print("1.sum,2.sub,3.mul,4.div,5.mod,6.exit")
    choice=int(input("enter a choice number"))
    if choice==1:
        print("sum of 2 number",NO1+NO2)
    elif choice==2:
        print("sub of 2 number",NO1-NO2)
    elif choice==3:
        print("multi of 2 number",NO1*NO2)
    elif choice==4:
        print("div of 2 number",NO1/NO2)
    elif choice==5:
        print("mod of 2 number",NO1%NO2)
    elif choice==6:
        break