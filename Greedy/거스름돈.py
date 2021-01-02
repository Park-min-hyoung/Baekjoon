rest_money = 1000 - int(input())
count = 0

money = [500, 100, 50, 10, 5, 1]

for i in money:
    count += (rest_money // i)
    rest_money %= i
print(count)