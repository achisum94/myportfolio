
number_of_exams=4
#ask from the user each exam score
exam1=int(input('enter the first exam result: '))
exam2=int(input('enter the second exam result: '))
exam3=int(input('enter the third exam result: '))
exam4=int(input('enter the forth exam result: '))

#get the total of all exams
total=exam1+exam2+exam3+exam4
average_score=total/number_of_exams

if average_score>=50:
    print('the student passed the semester')
else:
    print('the student failed the semester')