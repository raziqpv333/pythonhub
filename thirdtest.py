p=int(input("enter your roll no"))
z=int(input("enter you age"))
s=input("enter your name")
print(p,z,s)
l=[]
l.extend([p,z,s])
print(l)

l=[10,20,30,40,50]
p=int(input("enter your number"))
if p in l:
    print("available")
else:
    print("not available")
   



l=[10,20,10,1,2,1,2,3]
n=[]
for item in l:
    if item not in n:
        n.append(item)
print(n)