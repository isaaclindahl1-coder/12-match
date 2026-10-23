#The good old if/elif/else:
#I have a number representing the days of the week
# (1-7) (sun-sat) respectively
#
# Write me a function called get_day_name_if_else(num)
# it will take a num and will returne a days name (eg. 1 will return sunday)
# use if/elif/else:

#if / elif / else
def get_day_name_if_else(num):
    userinput = input("choose a day number (1 through 7): ")
    if num == 1:
        print("sunday")
    elif num == 2:
        print("monday")
    elif num == 3:
        print("tuesday")
    elif num == 4:
        print("Wensday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
    else:
        print("Invalid number.")

#A match-case statement is an alternative to using mulipule if elif and else statements
#It works by comparing a value (the "match") against several possible patternes (the "case")
#When a match is found, the under that case runs
def get_day_name_match(num):
    match num:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wensday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _: #like the else
            print("Not a valid day")


get_day_name_match(1)
get_day_name_match(9)
get_day_name_match("test")

def is_weekend(daystr:str) -> bool:
    match daystr:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wensday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False

def is_weekend_shorter_match(daystr:str) -> bool:
    match daystr:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wensday" | "Thursday" | "Friday":
            return False
        case _:
            raise ValueError("Thats not a day, stupid!")
        

print(is_weekend("Sunday"))
print(is_weekend("Monday"))
print(is_weekend_shorter_match("Sunday"))
print(is_weekend_shorter_match("Monday"))
print(is_weekend_shorter_match(":)"))