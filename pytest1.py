r=int(input("enter a number"))
g=int(input("enter a number"))
s=0
v=0
q=0
for i in range(r,g):
    s +=i
    if i%2==0:
            v +=i
    else:
          q +=i

print("sum of normal number is=",s)  
print("sum of even  number is =",v)
print("sum of odd number is=",q)
         

  
