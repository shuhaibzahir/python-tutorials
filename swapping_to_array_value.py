

size = int(input("please enter a input  "))
array1 = []
for i in range(size):
    value = input(f"enter value for array 1 index of {i}  ")
    array1.append(value)

array2 = []
for i in range(size):
    value = input(f"enter value for array 2 index of {i}  ")
    array2.append(value)
    
    
print("this is array 1 ", array1)
print("this is array 2 ", array2)

for i in range(size):
    temp = array1[i]
    array1[i]=array2[i]
    array2[i]=temp
print("after swapping---------------------------------")
print("this is array 1 ", array1)
print("this is array 2 ", array2)
    

