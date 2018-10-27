#get number of students who passed
passed=int(input('enter number of students that passed the exam: '))
#get number of students who failed
failed=int(input('enter number of students that failed in the exam: '))
#total number of students in the class
total=passed+failed
print('total of students: ',total)
# get percentages
pass_percentage=passed/total
fail_percentage=failed/total

print(format(pass_percentage, '%'),'of students passed in the class')
print(format(fail_percentage,'%'), 'of students failed in the class')