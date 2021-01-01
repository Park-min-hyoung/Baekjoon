inp = int(input())
suger = 0

while True:
    if inp % 5 == 0:
        suger += (inp // 5)
        print(suger)
        break
    inp -= 3
    suger += 1
    if inp % 5 != 0 or inp % 3 != 0:
        print(-1)
        break

# 틀렸다
# 이런 유형의 문제는 가장 큰 값을 이용해야 한다. 내가 그냥 5로만 나눠서 숫자로 빨리 작게 만들어야지 생각만해서 문제가 안풀렸다
# 큰 수(5)로 나누어 주어야 하지만 깔끔하게 나눠질 수 있도록 3을 빼주고 5로 나눠지면 깔끔하다


