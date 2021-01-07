men = int(input())

tip = []
for i in range(men):
    tip.append(int(input()))

tip.sort(reverse=True)
sum = 0
for i in range(len(tip)):
    if tip[i] - i > 0:
        sum += tip[i] - i
print(sum)