tup=(10,"shriya",20, 60, 80.4,20)
print(tup)
print(len(tup))
print(tup[4])
print(tup[-5:-1])#slicing: access multiple elements
tup2=(2,40,5,90,45)
print(tup+tup2)# concatanation
print(tup.count(20))
print(tup.index("shriya"))
print(min(tup2))
print(max(tup2))
print(sum(tup2))
print( 20 in tup)
for i in tup:
    print(i)