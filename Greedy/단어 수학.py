import sys
input = sys.stdin.readline

n = int(input())
value = []
for i in range(n): value.append(list(input().strip()))

a = [0 for _ in range(26)]
for i in value:
    li = len(i)

    for j in range(li): a[ord(i[j]) - 65] += 10 ** (li - j - 1)
a.sort(reverse=True)

sum = 0
for i in range(9, -1, -1):
    sum += (i * a[9 - i])
print(sum)

# 틀렸다
''' 나의 해결 : 이번에도 답은 나왔지만 런타임 에러라고 한다 뭐가 문제 일까??? (런타임 에러 질문)'''
'''아이디어 : 1. 이번 문제는 아이디어 조차 발견 못했다. 앞으로 알파벳 문제가 나오면 A~Z까지 중요도(수의자리가 높음)를 나타내는 것이 제일먼저
2. 알파벳 별로 중요도가 높은 순서대로 9부터 1까지 곱해서 더해주면된다'''