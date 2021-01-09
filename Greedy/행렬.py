n, m = map(int, input().split())

before = [[int(x) for x in input()] for _ in range(n)]
after = [[int(x) for x in input()] for _ in range(n)]

cnt = 0
def check():
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                return False
    return True

def solve(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            before[i][j] = 1 - before[i][j]

for i in range(n - 2):
    for j in range(m - 2):
        if before[i][j] != after[i][j]:
            cnt += 1
            solve(i, j)

if check(): print(cnt)
else: print(-1)

# 틀렸음
'''나의 해결 : 틀렸다'''
'''해결 아이디어
1. check 함수를 통해 뒤집기 작업이 다 끝난뒤에 A배열과 B배열을 비교해 다른 원소가 하나라도 있으면 False 리턴하고 한개라도 없으면 True를 리턴한다.
2. solve 함수를 통해 3 x 3의 왼쪽 상단의 x, y 좌표를 받아와서 뒤집기 작업을 해준다.
3. 3 x 3의 왼쪽 상단 부분만 다르다면 3 X 3을 모두 바꾸어주어야 하므로 카운터가 올라가고 solve 메소드를 호출함으로써 작업을 시작한다
4. check 함수의 리턴 값이 True이면 A, B가 똑같도록 작업이 끝났으므로 카운터를 출력하고 False이면 두 배열이 아직 같지 않으므로 -1을 출력한다
5. 복잡한거는 함수로 고민해보는 것도 좋은 방법인 것 같다'''