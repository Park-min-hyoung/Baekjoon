money = int(input())

cnt = 0
if money % 5 == 0: cnt += money // 5
else:
    while True:
        money -= 2
        cnt += 1
        if money % 5 == 0:
            cnt += money // 5
            break
        if money < 0:
            cnt = -1
            break
print(cnt)

''' 반복문을 사용하지 않고 해결 하는 방법
money = int(input())

result = 0
rest = money % 5

if money == 1 or money == 3: result = -1
elif rest % 2 == 0:
    rest = money // 5 + rest // 2
else:
    rest = ((money // 5) - 1) + ((rest + 5) // 2)

print(rest)
'''