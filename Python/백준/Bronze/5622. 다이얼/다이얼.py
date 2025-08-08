dic_d = {
    "2" : ['A','B','C'],
    "3" : ['D','E','F'],
    "4" : ['G','H','I'],
    "5" : ['J','K','L'],
    "6" : ['M','N','O'],
    "7" : ['P','Q','R','S'],
    "8" : ['T','U','V'],
    "9" : ['W','X','Y', 'Z']
}
# 1: 2초 2: 3초 ...


chars = input()
numbers = ""
for c in chars:
    for k in dic_d.keys():
        if c in dic_d[k]:
            numbers += k
sec = 0
for i in range(len(numbers)):
    sec += int(numbers[i])+1
print(sec)