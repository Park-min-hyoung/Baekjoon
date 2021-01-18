n, m, k = map(int, input().split())

for i in range(n):
    for j in range(m):
        v = ((m - 1) * i) + (i + j)
        if v == k:
            print(i, j)
            break

'''쉽게 푸는 방법
n, m, k = map(int, input().split())
a = k // m
b = k % m
print(a, b)
'''