n, k = map(int, input().split())
count = 0
value = []
for i in range(n):
    value.append(int(input()))

value.reverse()

for i in value:
    count += (k // int(i))
    k %= i
print(count)

# 맞았다