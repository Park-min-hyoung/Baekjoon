n, l, k = map(int, input().split())

test = []
for i in range(n):
    a, b = map(int, input().split())
    test.append([a, b])

    test = sorted(test, key = lambda a : a[1])

score = 0
while k != 0:
    if l >= test[0][1]:
        score += 140
        del test[0]
    else:
        test = sorted(test, key=lambda a: a[0])
        if l >= test[0][0]:
            score += 100
            del test[0]
    k -= 1
print(score)