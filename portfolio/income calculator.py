income=int(input('enter the income: '))
frequency=int(input('enter the frequency: '))
months=12

monthly_income=(income*frequency)/months
monthly_payment=int(input('enter the monthly payment: '))
pti=(monthly_payment/monthly_income)

print('mth income: ',monthly_income)
print('pti: ',pti)