value = input().split('-')
num = []

for i in value:
    cnt = 0
    s = i.split('+')

    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(value)):
    n -= num[i]
print(n)

# 틀렸음
# -를 기준으로 나누는 것은 좋은 아이디어 였고 방법이 있을거야(지금은 모르겠어), 이 방법은 - 를 기준으로 나눈 배열을 각각 또 +로 나눠서 각각의 값을 더해준다음
# num 배열에 저장한다음 계산한다.(eval()을 쓰면 안되나...)
