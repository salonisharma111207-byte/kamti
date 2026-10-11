s={10,20,30,40,50,"saloni",20}
print(s)
print(type(s))
print(len(s))

s.add("pretty")       # add element
print(s)

s.remove(40)          # remove element
print(s)

s.discard(70)         # no error if element is absent
print(s)

s.pop()               # remove one arbitrary element
print(s)

s.clear()             # empty the set
print(s)

s1={10,20,30,40,50,10}
s2={100,80,90, 40, 50,70}
print(s1.union(s2))
print(s1|s2)

print(s1.intersection(s2)) # alo use & operator

print(s1-s2)#difference
print(s2. issubset(s1))
print (s2.isdisjoint(s1))#no common elements
print(s1^s2)# not common elements