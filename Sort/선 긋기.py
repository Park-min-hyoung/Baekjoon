n = int(input())

data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
data.sort()

start = data[0][0]
end = data[0][1]
length = 0
for i in range(1, n):
    if data[i][0] > end: # 다음 시작점의 좌표가 end 보다 클때(주어진 좌표가 현재 범위에 속하지 않는다)
        length += (end - start)
        start = data[i][0]
        end = data[i][1]
    else: # 주어진 좌표가 현재 범위에 속할때
        if data[i][1] > end:
            end = data[i][1]

print(length + (end - start))

# 틀렸음
'''나의 해결 : 도움 받아서 맞추기는 했음'''
'''해결 아이디어
1. 시작점을 기준으로 오름차순을 하게되면 다음 좌표가 지금 범위에 있지 않은 것을 제외하고는 start가 변하지 않으므로
end로만 조정 해주면 된다.'''

'''문제
1. 선을 그을 때에는 자의 한 점에서 다른 한점까지 긋게 된다.
2. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그읏 곳의 차이를 구별할 수 없다고 하자
3. 이와 같은 식으로 선을 그었을 때, 그려진 선들의 총 길이를 구하는 프로그램(선이 여러번 그려진 곳은 한 번씩만 계산)'''