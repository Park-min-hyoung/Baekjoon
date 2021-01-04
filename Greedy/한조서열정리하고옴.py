n = int(input())
mount = list(map(int, input().split()))
ma = 0
cnt = -1
kill = []

for i in range(len(mount)):
    if ma < mount[i]:
        ma = mount[i]
        kill.append(cnt)
        cnt = 0
    else: cnt += 1
if ma > mount[n - 1]: kill.append(cnt)

print(max(kill))