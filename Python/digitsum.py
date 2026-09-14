# digit sum
num=1234
digitsum=0
while num > 0:
    lastdigit = num%10
    digitsum += lastdigit
    num= num//10
print("sum of digit of number is: ",digitsum)    