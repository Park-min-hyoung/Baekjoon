n = int(input())
left = list(map(int, input().split()))

men = []
for i in range(len(left) - 1, -1, -1):
    if i == len(left) - 1: men.append(i + 1)
    else: men.insert(left[i], i + 1)

for i in men:
    print(i, end = ' ')