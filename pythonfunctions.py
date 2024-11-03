def inputGrades(nm):
    grades=[]
    for i in range(0,nm,1):
       grade = float(input('what are the grades? '))
       grades.append(grade)
    return grades

def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])

def avrGrades(nm,x):
    tot=0
    for i in range(0,nm,1):
        tot = tot + x[i]
    avr= tot/nm
    return avr

def hiGradeLowGrade(nm,x):
    hiGrd=0
    lowGrd=100
    for i in range(0,nm,1):
        if x[i] > hiGrd:
            hiGrd = x[i]
        if x[i] < lowGrd:
            lowGrd = x[i]
    return hiGrd,lowGrd

numGrades= int(input('how many grades do you have? '))
print('')

myGrades = inputGrades(numGrades)
print('')

print('your grades are: ')
printGrades(numGrades,myGrades)

average=avrGrades(numGrades,myGrades)
print('your average grade is: ',round(average,2))

hiGrade,lowGrade = hiGradeLowGrade(numGrades,myGrades)
print('your high grade is:',hiGrade)
print('your low grade is:',lowGrade)