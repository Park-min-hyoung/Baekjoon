n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

for i in range(n):
    for j in range(2):
        print(s[i][j], end = ' ')
    print()

last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)

# 틀렸다
# 값을 한줄씩 넣은 다음에 시작 시간과 끝나는 시간이 같을 수 있으므로 시작 시간을 오름차순 해준 다음 끝나는 시간을 오름차순 해준다
# 내가한거는 시작시간만 오름차순으로 정렬됬어.. i(시작시간)가 last(종료시간)보다 크거나 같으면 cnt(회의 수)를 올려주면 된다.
# 한 쪽만 고집하지 말고 다른 쪽도 시도 해보자(이 문제 같은 경우 시작 시간만 오름차순으로 하려고 하다보니 문제가 안풀렸어)
