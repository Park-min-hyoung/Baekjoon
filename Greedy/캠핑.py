camp = []
while True:
    l, p, v = map(int, input().split())
    camp.append([l, p, v])
    if l + p + v == 0: break

for i in range(len(camp) - 1):
    sum = camp[i][2] // camp[i][1]
    temp = min(camp[i][2] % camp[i][1], camp[i][0])
    sum = camp[i][0] * sum + temp
    print('Case %d: %d' %(i + 1, sum))