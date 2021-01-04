market = int(input())
milk = list(map(int, input().split()))
cnt = 1
s = milk.index(0)
ms = milk[s]

for i in range(s + 1, len(milk)):
    if ms == 0 and milk[i] == 1:
        cnt += 1
        ms = 1
    elif ms == 1 and milk[i] == 2:
        cnt += 1
        ms = 2
    elif ms == 2 and milk[i] == 0:
        cnt += 1
        ms = 0
print(cnt)