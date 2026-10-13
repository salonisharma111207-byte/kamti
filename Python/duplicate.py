l=[10,20,10,40,50,60,10,20]
unique=list(set(l))
print (unique)

#second method
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)        