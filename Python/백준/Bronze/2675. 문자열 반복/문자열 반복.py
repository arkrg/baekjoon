tc_time = int(input())
result = []
for _ in range(tc_time):
    r = ""
    r_time, string = "", ""
    r_time, string = input().split()
    for s in string:
        r +=s*int(r_time)
    result.append(r)
for r in result:
    print(r)