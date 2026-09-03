#string
fruit="mango"
print("my favourite fruit is"+fruit)
#print letter by indexing
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
#print letter from back side
print(fruit[-1])
print(fruit[-2])
print(fruit[-3])
print(fruit[-4])
#print character using loop
for letter in fruit:
    print(letter)
#length of string
print("length of fruit is=",len(fruit))    
print(fruit[0:4])
print(fruit[:3])
print(fruit[-3:-1])
# STRING METHODS,STRING ARE IMMUTABLE
a="sally bhai !"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("sally","sallu"))
print(a.index("bhai"))
