month=input("enter month name: ")
match month:
    case "december"|"january"|"february":
        print("winter season")
    case "march"|"april":
        print("spring season")
    case "may"|"june"|"july":
        print("summer season")
    case "august"|"september":
        print("rainy season")
    case "october"|"november":
        print("autumn season")            
    case _:
        print("this is not a month")    