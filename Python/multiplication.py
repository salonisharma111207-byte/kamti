# for i in range(1,11):
#     print ("5*",i,"=" ,5*i)

#     #reverse number
# for i in range (10,0,-1):
#     print(i)

#even number
# for i in range(1,51):
#     if(i%2==0):
#         print(i)

#sum of natural number
# sum=0
# for i in range (1,101):
#     sum+=i
# print(sum)

# #from user input
# n=int(input("enter any number:"))
# for i in range(n):
#     print(i+1)

# # divisible by 3
# for i in range(1,100):
#     if (i%3==0):
#         print(i)

#factorial
# fact=1
# n=int(input("enter any number:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial of",n,"is: ",fact)

#factor
#  n=int(input("eneter any number: "))
#  for i in range(1,n+1):
#      if(n%i==0):
#     print(i)

#largest number
largest=0
for n in range(5):
    n=int(input("enter number:"))

    if (n>largest):
       largest=n
print("largest no. is:",largest)