n, l = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

cnt = 0
mi = x[0]
for i in range(len(x) - 1):
    if x[i + 1] - mi + 1 <= l:
        continue
    else:
        cnt += 1
        mi = x[i + 1]
print(cnt + 1)