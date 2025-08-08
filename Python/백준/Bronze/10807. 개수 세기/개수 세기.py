tc_count = int(input())
inteters = []
integers = input().split()
target = int(input())

count = 0
for i in integers:
    if int(i) == target:
        count += 1

print(count)