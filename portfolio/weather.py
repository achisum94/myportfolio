#we are going to write in in Caps

NUM_DAYS=7

max_temp=0
min_temp=100

for i in range(NUM_DAYS):
    print('enter the temperature for day',i+1)
    temp=int(input())
    if temp>max_temp:
        max_temp=temp
        hottest=i+1
    if temp<min_temp:
        min_temp=temp
        coldest=i+1
print('the hottest day is: day',hottest)
print()       
print('the coldest day is: day',coldest)       