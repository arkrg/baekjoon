a, b, c = map(int, input().split())
same_count = 1
eyes = []
eyes.append(a)
if b in eyes:
    same_count+=1
    eye=b
else: 
    eyes.append(b)
if c in eyes:
    same_count+=1
    eye=c
else: 
    eyes.append(c)

max_value = max(eyes)
if(same_count==3):
    prise = 10000+eye*1000
elif(same_count==2):
    prise = 1000 + eye*100
else:
    prise = max_value*100

print(prise)
    