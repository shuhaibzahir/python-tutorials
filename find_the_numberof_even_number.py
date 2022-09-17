#find the number of even number in an array 

size = int(input("enter your size of array  "))
array = []


for i in range(size):
    value = int(input(f"the input for index {i} "))
    array.append(value)
    
def count_event_number(array):
    count=0
    for i in range(size):
        if array[i]%2==0:
            count+=1
    return count
            

print(f"the count of even number is {count_event_number(array)}")