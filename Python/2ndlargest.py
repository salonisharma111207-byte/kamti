number=[10,40,60,20,80,50]
largest=float("-inf")
second_largest=float("-inf")
for i in number:
    if i >largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i<largest:
        second_largest=i
print("second largest number in list is: ",second_largest)           