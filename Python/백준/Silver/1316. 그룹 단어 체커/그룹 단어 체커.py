test_count = int(input())
group_count = 0

for i in range(test_count):
    test_case = input()
    is_nice = True
    new = []
    new.append(test_case[0])
    for i in range(len(test_case)-1):
        if test_case[i] != test_case[i+1]:
            if test_case[i+1] in new:
                is_nice = False
                break
            else:
                new.append(test_case[i+1])
    if is_nice:
        group_count += 1
    
print(group_count)