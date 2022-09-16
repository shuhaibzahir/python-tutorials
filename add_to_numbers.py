# 2. Accept two inputs from the user and output its sum.

    


def add_to_numbers():
    try:
        #converting string to number and float
        num1 = input("enter your first number 'integer not float'        : ")
        num2 = input("enter your second number float            :  ")
        if(num1 == "exit"):
            return "your are exited"
        else:
            number1 = int(num1)
            number2 = float(num2)
            return number1 + number2
    except ValueError:
        print("please enter valid values and if you don't want continue type exit")
        return add_to_numbers()

sum =  add_to_numbers()
print(sum)
        
        