number_of_incometypes=4
exam1=int(input('enter the bi-weekly payment: '))
exam2=int(input('enter the frequency: '))
exam3=12

monthly_income=(exam1*exam2)/exam3
monthly_payment=int(input('enter the monthly payment: '))
pti=(monthly_payment/monthly_income)

print('mth income: ',monthly_income)
print('pti: ',pti)