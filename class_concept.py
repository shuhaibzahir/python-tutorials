
class Test:
    def __init__(self,number1, number2):
        self.num1 = number1
        self.num2 = number2
    def add_to_numbers(self):
        print(f"this is sum {self.num1 + self.num2}")
    def substract(self):
        print(f"this is substract {self.num1 - self.num2}")
    def multi(self):
        print(f"this is multi value {self.num1 * self.num2}")
    def division(self):
        if(self.num1 > 0 and self.num2 > 0):
            print(f"this is division {self.num1 / self.num2}")
        else:
            print("invalid values")

def class_test():
    number1 = int(input('enter your first number '))
    number2 = int(input('enter your second number '))
    
    choice = int(input("enter number  \n 1: add \n 2: sub \n 3: multi \n 4: division \n"))
    math_class = Test(number1,number2)
    match choice:
        case 1: 
            math_class.add_to_numbers()
        case 2:
            math_class.substract()
        case 3:
            math_class.multi()
        case 4:
            math_class.division()
        case _:
            print("invalid input")
        
class_test()
            
        
        

    