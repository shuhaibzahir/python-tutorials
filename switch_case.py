 #Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 

number = int(input("enter your input"))

match number:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("not valid entry")