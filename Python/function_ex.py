#check length of the given string
def check_length(string):
    return len(string)>5
        
string=input("enter text:")
print(check_length(string)) 

#leap year
def is_leap_year(year):
    return (year % 4==0 and year % 100!=0)or(year%400==0)
year=int(input("eneter any year: "))
print(f"{year}is leap year :",is_leap_year(year))