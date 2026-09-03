num1=float(input("enter first number: "))
operator=input("enter operator'(+,-,*,/,%)': ")
num2=float(input("enter second number: "))
match operator:
    case"+":
        print(f"result={num1+num2}")
    case"-":
        print(f"result={num1-num2}")  
    case"*":
        print(f"result={num1*num2}")   
    case"/":
        if num2!=0:
           print(f"result={num1/num2}")
        else:
            print("error: can't divide by zero")   
    case"%":
        print(f"result={num1+num2}")  
    case _:
        print("you choose wrong operator")                        