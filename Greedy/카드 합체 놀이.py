n, m = map(int, input().split())
num = list(map(int, input().split()))

for i in range(m):
    num.sort()
    s = num[0] + num[1]
    num[0] = s
    num[1] = s
print(sum(num))