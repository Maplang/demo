numberOfGrades = int(input('How many subjects do you do: '))
grades = []
gradeSum = 0

for i in range(0,(numberOfGrades),1):
    grade = (input('what are the grades: '))
    grades.append(grade)
print('your grades are: ')
for i in range(0,(numberOfGrades),1):
    print(grades[i])
for i in range(0,(numberOfGrades),1):
   gradeSum = (gradeSum+float( grades[i]))
gradeAvr = gradeSum/numberOfGrades   
print ('And your grade average is ', gradeAvr)