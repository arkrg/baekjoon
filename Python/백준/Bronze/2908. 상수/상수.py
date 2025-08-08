n1, n2 = input().split()
s_n1, s_n2 = "", ""
for i in range(1,len(n1)+1):
    s_n1 += n1[-i]
    s_n2 += n2[-i]

print (s_n1 if int(s_n1) > int(s_n2) else s_n2)