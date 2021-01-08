import sys

n = int(input())
length = list(map(int, input().split()))
money = list(map(int, input().split()))

mi = sys.maxsize

value = 0
for i in range(n - 1):
    mi = min(mi, money[i])
    value += mi * length[i]
print(value)

# 틀렸음
'''나의 해결 : 입력하는 족족 올바른 출력은 나오는데 뭐가 틀린지 모르겠다 틀린게 있겠지'''
'''해결 아이디어
1. 최소값 변수(mi)에 정수중 가장 큰 값을 넣어준다
2. 내가 생각한 것은 미리 최소값을 알아내는 방법이지만 for문을 돌리면서 최소값을 money의 최소값을 변경해줌으로써 연산해주는 방법도 있다. '''