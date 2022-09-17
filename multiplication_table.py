#Write a program to print the multiplication table of given numbers.

user_input = int(input("enter your number  "))

for i in range(0,11):
    print(f"{i} * {user_input} = {i * user_input}")