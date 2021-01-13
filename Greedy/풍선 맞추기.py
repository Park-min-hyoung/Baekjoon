n = int(input())
ball_check = [0 for _ in range(n + 1)]
ball = list(map(int, input().split()))

cnt = 0
for i in ball:
    if ball_check[i] == 0:
        cnt += 1
        ball_check[i - 1] += 1
    elif ball_check[i] > 0:
        ball_check[i] -= 1 # 해당 높이의 풍선을 터트리고
        ball_check[i - 1] += 1 # 해당 높이 -1에 풍선이 추가된다?
print(cnt)

# 틀렸음
'''나의 해결 : 못풀었다 엄청 어렵다'''
'''해결 아이디어
1. 모든 원소가 0으로 초기화 된 n + 1 크기의 배열 생성
2. 높이 수치에 해당하는 인덱스가 0이라면 h(높이)에 화살이 온적이 없기 때문에 풍선이 터지면서 카운터가 올라가고 h-1 높이로 화살이 향한다.
3. 높이 수치에 해당하는 인덱스가 0보다 크다면 h에 화살이 왔기 때문에 풍선은 터지지만 이미 온 화살이기 때문에 카운터는 올라가지 않고
 풍선이 터지면서 h-1 높이로 화살이 향한다'''