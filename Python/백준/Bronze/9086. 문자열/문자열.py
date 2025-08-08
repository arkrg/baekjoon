tc_num = int(input())
results = []
for _ in range(tc_num):
    s = input()
    results.append(f"{s[0]}{s[-1]}")

for r in results:
    print(r)