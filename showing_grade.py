#Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
total_mark = float(input("Enter your total mark percentage      "))

def check_grade(percentage):
    if percentage < 50 :
        return "failed"
    elif percentage >= 50 and percentage < 60:
        return "E"
    elif percentage >= 60 and percentage < 70:
        return "D"
    elif percentage >= 70 and percentage < 80:
        return "C"
    elif percentage >= 80 and percentage < 90:
        return "B"
    elif percentage >= 90 and percentage <= 100:
        return "A"
    else:
        return "wrong input"
    
percentage = check_grade(total_mark)
print(percentage)



 
