my_name="saloni sharma"
match my_name:
    case int():
        print("it is an integer type,it's double will:",my_name*2)
    case float():
        print("it is a float data type")
    case str():
        print("it is a string type and length of given string is:",len(my_name))
    case _:
        print("it is an another data type")    