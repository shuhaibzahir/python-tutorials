user_input = int(input("enter your input  "))
sum =0

for i in range(user_input+1):
    if i%2!=0:
        sum+=i

print(sum)