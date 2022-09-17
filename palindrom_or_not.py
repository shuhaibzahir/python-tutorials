import math


user_input = input("enter your input to check is palindrom:   ")
palindrom = True
user_input_len = len(user_input)
for i in range(math.ceil(user_input_len/2)):
    if user_input[i]!= user_input[user_input_len-i-1]:
        palindrom = False
print(f"this is {palindrom if 'palindrom ' else 'not palindrom'}")
        
        

