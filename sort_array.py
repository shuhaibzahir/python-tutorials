#  Write a program to sort an array in descending order

size = int(input("enter the size of array  "))

array =[]
for i in range(size):
    value = int(input(f"input for index {i} "))
    array.append(value)

array= sorted(array, reverse=True)
#array.sort(reverse=True)

print(array)

