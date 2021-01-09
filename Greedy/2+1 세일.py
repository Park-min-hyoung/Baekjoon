n = int(input())

money = []
for i in range(n):
    money.append(int(input()))
money.sort(reverse=True)

sum = 0
for i in range(len(money)):
    if (i + 1) % 3 != 0:
        sum += money[i]
print(sum)