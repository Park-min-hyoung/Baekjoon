n = int(input())
data = list(map(int, input().split()))

target = 0
while True:
    up_cnt = 0
    down_cnt = 0
    for i in data:
        if i > target:
            up_cnt += 1
        if i == target:
            if up_cnt >= target: down_cnt += 1
            else: up_cnt += 1
        if i < target:
            down_cnt += 1

    if up_cnt >= target and down_cnt >= n - target:
        print(target)
        break

    target += 1

# 틀렸음
'''나의 해결 : 틀렸다 못 풀었다'''
'''문제 아이디어
1. 나중에 다시 풀어보기'''

'''문제
1. 발표한 논문과 그 논문들의 인용횟수를 고려한 학위 취득 조건을 만족해야 한다
2. 논문들의 중요도를 측정하기 위해, 가장 많이 인용된 논문들의 개수와 그 논문들의 인용횟수를 이용하여 정의
3. k번 이상 인용된 논문이 k편 이상이고 나머지 n - k편의 논문들 인용횟수가 각각 k번 이하라면, 해당 학생의 q-인덱스는 k이다.'''