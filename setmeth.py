s={1,4,5,6,7}
print(s)
s={51,22,5,4,7}
s.update({40,506,55})
print(s)
s={50,122,5,4,17}
s.add(76)
print(s)
s={50,122,5}
s.discard(1)
print(s)
s={11,14,5,6,7}
s.remove(11)
print(s)
s={50,122,5,4,17}
s.clear
print(s)
s={50,122,5,4,17}
s.pop
print(s)

s={10,101,120,130}
print(s.difference({10}))
s={10,101,120,133}
print(s.intersection({10,20}))
s={10,101,150,130}
print(s.isdisjoint({50,60}))
s={10,101,120,130}
print(s.issubset({50,70}))
s={10,101,120,130}
print(s.issuperset({40,5}))
s={10,101,120,130}
print(s.symmetric_difference({10,50,60}))
s={10,101,120,130}
print(s.union({50,60,90}))
s={10,101,120,130}
s.difference_update({40,50,44})
print(s)
s={10,101,120,130}
s.symmetric_difference_update({41,55})
print(s)
s={10,101,120,130}
s.intersection_update({50,55})
print(s)