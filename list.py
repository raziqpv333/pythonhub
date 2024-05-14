l=[10,20,30,"apple","red",15.5,True,70]
l1=[]
for i in l:
    print(i)
if 20 in l:
     print("yes")
else:
       print("no")

print(l[0])
print(l[-1])
print(l[:3])
l[0]=50
print(l)  
del l[0]   
print(l)
    

        