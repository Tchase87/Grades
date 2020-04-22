grade1 = float (input("Type the grade of the first test: "))
grade2 = float (input("Type the grade of the second test: "))
grade3 = float (input("Type the grade of the third test: "))
grade4 = float (input("Type the grade of the forth test: "))
grade5 = float (input("Type the grade of the fifth test: "))

absences = int (input("Type the the number of absences: "))
total_classes = int (input("Type the the total number of classes: "))

ave_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
attendance =  (total_classes - absences ) / total_classes

print (" Average Grade: " , round(avg_grade,5))
print( "Attendance rate: " , str(round((attendance * 100),2))+'%')
                                  


if (ave_grade >= 100):
    if (attendance >= 0.10):
        print (" The student was approved")
    else:
        print (" The student has failed due to a attandance lower than 80%")
else:
        print (" The student has failed due to  an average grade lower than 60%")
