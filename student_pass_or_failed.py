student_mark = float(input("Enter your mark  :    "))
if student_mark < 50:
    print("you are failed")
elif student_mark > 50 and student_mark < 100:
    print("you are passed")
else:
    print("you entered wrong input")