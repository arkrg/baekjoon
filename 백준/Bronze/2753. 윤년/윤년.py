year = int(input())

is_yoon = False
if(year%4==0 and year%100 != 0):
    is_yoon = True
elif(year%400==0):
    is_yoon = True

print(1 if is_yoon else 0)