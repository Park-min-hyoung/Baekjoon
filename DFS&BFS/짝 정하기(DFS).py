n = int(input())

check = True
data = []
for i in range(3):
    a, b = map(int, input().split())
    data.append(a)
    data.append(b)

for i in range(data[0] + 1):
    a = i
    d = data[0] - a
    e = data[5] - d
    b = data[2] - e
    c = data[1] - b
    f = data[4] - c

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        check = False
        break

if check:
    print(0)

# 틀렸음
'''나의 풀이 : 틀렸음'''
'''아이디어: 
1. https://settembre.tistory.com/73
2. 이거 좀 어렵다 아니 많이 어렵다'''




'''문제
1. 서로 모르는 학생끼리 짝이 되도록 하기 위해 같은 초등학교 출신이 아닌 남학생과 여학생을 짝으로 정하기로 원칙
'''

'''입력
1. 3 ≤ 학생의 수 ≤ 100,000'''