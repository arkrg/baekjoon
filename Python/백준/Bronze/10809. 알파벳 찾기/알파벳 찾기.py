string = input()
new = []
for i in range(ord("z")-ord("a")+1):
    target = chr(i+ord("a"))
    is_hit = False
    for j in range(len(string)):
        if string[j] == target:
            if target in new:
                continue
            is_hit = True
            print(j, end = " ")
            new.append(target)
        if j==len(string)-1 and is_hit==False:
            print("-1", end = " ")
            