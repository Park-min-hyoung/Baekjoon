n, m = map(int, input().split())

if n == 1: print(1)
elif n == 2: print(min(4, (m + 1) // 2))
else:
    if m <= 6: print(min(4, m))
    else: print(m - 2)

# 틀렸음
'''나의 해결 : 물론 내가 한게 답은 나오겠지만 큰 수에서는 시간이 너무 많이 걸리므로 시간초과가 발생하므로 틀린답이다'''
'''해결 아이디어
1. 세로가 1개일때는 아무 방법도 사용할 수 없으므로 방문할 수 있는 곳은 자기위치 뿐이므로 1
2. 세로가 2개일때는 2,3번 방법만 사용할 수 있으므로 아무리 방문을 많이하더라도 4가 최대 값이다.
그러므로 2,3번 방법을 사용한 방문수는 (m + 1) // 2이므로 이 값과 4를 비교해서 작은 값을 출력해주면된다.
3. 세로가 3개이살일때는 모든 방법을 사용 할 수 있지만 가로에 개수에 따라 결과값이 달라진다
1) 가로가 6이하일때는 4가 최대 값이고 1,4번을 사용해야 최대값을 구할 수 있으므로 4와 m을 비교해서 작은 값을 출력한다
2) 가로가 6보다 클때는 m - 2의 값을 출력해주면 된다.
4. 반복문을 사용해서 시간초과가 걸린다면 조건문을 이용해서 접근해보자!!!'''
