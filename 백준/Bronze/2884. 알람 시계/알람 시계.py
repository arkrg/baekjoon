H, M = map(int, input().split())

if(M>=45):
    print(H,end=" ")
    print(M-45,end="\n")
else:
    if(H>=1): print(H-1, end=" ")
    else: print("23", end=" ")
    print(15+M,end="\n")