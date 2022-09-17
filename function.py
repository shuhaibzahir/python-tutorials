#  Write a program to accept an array and display it on the console using functions


def get_array(size):
    array = []
    for i in range(size):
         array.append(input(f"enter the value of index {i} "))
    return array
         
def display_array(array):
    print("this is your array", array)
        

def main_fun():
    input_size = int(input("enter your input  "))
    array1 = get_array(input_size)
    display_array(array1)

main_fun()
    
    

    