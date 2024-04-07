#if-else statement
#if obtained marks in a subject is >= 50 then student passes the course
Marks = float(input("Please enter otained marks: "))
if Marks >= 50:
    print("Passed.")
else:
    print("Failed.")

#Making a grading calculator    
#elife statement
Name = input("Enter name of subject: ")
totalMarks = int(input("Enter total marks: "))
obtMarks = float(input("Enter obtained marks: "))
percentage = (obtMarks/totalMarks) * 100
if percentage >= 90:
    print(Name, " ", percentage, " Grade: A")
elif percentage >= 80:
    print(Name, " ", percentage, " Grade: B")
elif percentage >= 70:
    print(Name, " ", percentage, " Grade: C")
elif percentage >= 60:
    print(Name, " ", percentage, " Grade: D")
else:
    print(Name, " ", percentage, " Failed")