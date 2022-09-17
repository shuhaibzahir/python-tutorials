


sizeof_array = int(input("enter the size of array"))


def add_value (size,array_name):
    array = []
    for i in range(size):
        temp_array = []
        for j in range(size):
            value = int (input(f"please enter the value for {array_name} index {i} {j} :  "))
            temp_array.append(value)
        array.append(temp_array)
    return array

array1 = add_value(sizeof_array,"array 1")
array2 = add_value(sizeof_array,"array 2")

print("array 1", array1)
print("array 2", array2)


sum_array =[]

for i in range(sizeof_array):
    for j in range(sizeof_array):
        sum = array1[i][j] + array2[i][j] 
        sum_array.append(sum)

print(sum_array)