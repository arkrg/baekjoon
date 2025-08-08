string = input()
string = string.lower()
alph_count = {}
for alph in string:
    if alph in alph_count:
        alph_count[alph] += 1
    else:
        alph_count[alph] = 1

max_count = max(alph_count.values())
t_max_count = 0
for k in alph_count.keys():
    if alph_count[k] == max_count:
        t_max_count += 1
        t = k.upper()

if t_max_count == 1:
    print(t)
else:
    print("?")