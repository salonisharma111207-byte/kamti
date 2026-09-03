a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
if(a+b>c and b+c>a and a+c>b):
    print("it can form valid triangle")
else:
    print("it can not form vallid triangle")    