a=int(input("enter a unit"))
if a<=100:
    print("no charge")
elif a<=200:
    a-=100
    print("charge",a*5)
else:
    a-=200
    amt=500+a*10
    print(amt)

   