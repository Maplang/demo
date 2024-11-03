numGrades = int(input('how many courses do you do? '))
grades = []
gradesSum = 0
maxGrade = 0
minGrade = 100
swp=0

for i in range(0,numGrades,1) :
    grade = input('what are the grades? ')
    grades.append(grade)
print('')

print('your grades are: ')
for i in range(0,numGrades,1) :
    print(grades[i])  
print('')

for  i in range(0,numGrades,1) : 
    gradesSum= gradesSum+float(grades[i])  
gradesAvr = gradesSum/numGrades
print('the average of your grades is: ',gradesAvr)

for  i in range(0,numGrades,1) :
    if float(grades[i]) >= maxGrade:
        maxGrade = float(grades[i])
print('your highest grade is: ',maxGrade)

for  i in range(0,numGrades,1) :
    if float(grades[i]) < minGrade:
        minGrade = float(grades[i])
print('your lowest grade is: ',minGrade)


for  i in range(0,numGrades-1,1) :
    for  i in range(0,numGrades-1,1) :
        if grades[i]<grades[i+1]:
          swp=grades[i]
          grades[i]=grades[i+1]
          grades[i+1]=swp

print('your grades in order: ')
for  i in range(0,numGrades,1) :
    print(grades[i])        