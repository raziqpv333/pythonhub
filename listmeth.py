a=[10,20,30,"red",10.2]
a.append("hello")
print(a)
a.append([50,60,70,80,90])
print(a)
a.extend([100,101,102])
print(a)
a.insert(4,"orange")
print(a)

l=[15,25,85]
l.pop()
print(l)

l=[40,50,85]
l.pop(1)
print(l)

l=[90,80,74,55,55,74,55]
l.remove(55)
print(l)

l=[100,55,74,5,5,5]
l.clear()
print(l)

l=[50,55,44,77,7,50,50]
print(l.count(50))


l=[80,80,60,55,4]
print(l.index(80))

l=[50,44,66,11,5]
l.sort()
print(l)

l=[90,80,70,60,50]
l.reverse()
print(l)

l=['i',"am","batman"]
l1=l
print(l1)
l1.pop()
print(l1,l)

l=["i","am","spiderman"]
l2=l.copy()
print(l2)
l2.pop()
print(l2,l)