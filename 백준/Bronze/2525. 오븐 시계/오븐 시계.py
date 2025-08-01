H, M = map(int, input().split())
C = int(input())

AH = C // 60
AM = C % 60

TM=AM+M
CH = TM//60 if (TM>=60) else 0
H = (H + AH + CH) % 24
M = TM%60
print(H,M)
