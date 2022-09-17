# Write a program to find the simple interest.
principle_amount = int(input("enter your principle amount "))
intrest_rate = float(input("Enter your intrest rate"))
number_of_years = float(input("Enter you number of years"))

simple_interest = principle_amount * intrest_rate * number_of_years

print("This is your simple interest" , simple_interest)
