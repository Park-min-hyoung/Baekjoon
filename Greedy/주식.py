case = int(input())
for i in range(case):
    day = int(input())
    value = list(map(int, input().split()))

    sum = 0
    max = 0
    for j in range(day - 1, -1, -1):
        if value[j] >= max:
            max = value[j]
        else:
            sum += max - value[j]
    print(sum)

# 틀렸음
'''나의 해결 : 틀렸다'''
'''해결 아이디어
1. 앞에서 부터 작업을 하면 최대값이 수정되었을때 이제까지 지나온 주가를 다 더해야 하고 다음 인덱스의 주가가 작은지 큰지에 따라 파냐 마냐가
결정되므로 복잡하다(답은 낼 수 있겠지만 나는 하지 못했다)
2. 뒤에서 부터 작업을 하면 max를 정해놓고 하기때문에 처음 마지막 인덱스에 max보다 모든 인덱스가 작으면 쭉가고 만약 큰게 나온다고 하더라도
max를 업데이트해서 그대로 쭉가면 된다.'''