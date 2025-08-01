total = int(input())
num = int(input())

total_com = 0
for _ in range(num):
    price, count = map(int, input().split())
    total_com += price*count
is_same = total == total_com    

print("Yes") if is_same else print("No")