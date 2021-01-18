n = int(input())
car = map(int, input().split())

cnt = 0
for i in car:
    if (n % 10) == i: cnt += 1

print(cnt)