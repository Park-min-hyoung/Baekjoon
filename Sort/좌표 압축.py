import sys

n = int(input())
data = list(map(int, input().split()))

c_data = []
for i in range(len(data)):
    c_data.append([data[i], i])
c_data.sort()

idx = -1
min_value = -sys.maxsize - 1
res_data = [0] * n
for i in c_data:
    if i[0] != min_value:
        idx += 1
    min_value = i[0]

    res_data[i[1]] = idx

print(*res_data)

''' 쉽게 푸는 방법
n = int(input())
data = list(map(int, input().split()))
res_data = list(sorted(set(data)))
res_data = {res_data[i]: i for i in range(len(res_data))}
print(*list(res_data[i] for i in data))
'''

'''문제
1. 수직선 위에 N개의 좌표 x1, x2,..., xn이 있다
2. xi를 좌표 압축한 결과 x'i의 값은 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다
'''