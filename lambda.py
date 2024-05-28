add=lambda a,b:a+b
print(add(10,15))
sub=lambda c,d:c-d
print(sub(10,5))


l=[1,2,3,4,5,6]
data=map(lambda a:a**2,l)
print(list(data))

l1=[1,2,3,4,5,6]
data1=filter(lambda a:a%2==0,l1)
print(list(data1))