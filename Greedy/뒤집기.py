s = input()
change = []
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        change.append(i)
isOdd = False
if len(change) % 2 == 1:
    isOdd = True

result = len(change) // 2
if isOdd:
    result += 1
print(result)

# 틀렸다
'''나의 해결 : 틀렸다 맞고 있다고 왜 안맞았냐고 자만하고 있었는데 틀린거였다 체크를 제대로 안했다.'''
'''문제 아이디어
0. 반환점
1. 0 > 1 또는 1 > 0으로 전환되는 index를 배열에 저장한다
2. 0 > 1 > 0 이면 index가 2개가 나올것이다 그냥 그때 2개를 구간으로 정해서 한번 뒤집다는 생각하면 되므로 짝수는 나누기 2
홀수는 나누기 2 한다음에 + 1'''