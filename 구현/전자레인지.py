n = int(input())

time = [300, 60, 10]

result = []
for i in time:
    result.append(n // i)
    n %= i

if n == 0:
    for i in result:
        print(i, end = ' ')
else: print(-1)

'''간단하게 푸는 방법
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) // 60 // 10
    print(A, B, C)
'''