#secret number guess

secret=7
while True:
    guess=int(input("guess the number between (1-10):" ))
    if guess <secret:
        print("this number is lower than secret")
    elif guess > secret:
        print("this number is higher than secret")
    else:
        print("correct")        