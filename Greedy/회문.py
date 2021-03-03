def secondcheck(left, right, txt):
    while left < right:
        if txt[left] == txt[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def firstcheck(left, right, txt):
    while left < right:
        if txt[left] == txt[right]:
            left += 1
            right -= 1
        else:
            check1 = secondcheck(left + 1, right, txt)
            check2 = secondcheck(left, right - 1, txt)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


n = int(input())

for i in range(n):
    txt = input()
    left = 0
    right = len(txt) - 1
    ans = firstcheck(left, right, txt)
    print(ans)

# 틀렸음
'''나의 풀이 : 답은 나왔지만 시간 초과이므로 틀린거다'''
'''해결 아이디어
1. 첫 글자를 left로 하고 마지막 글자를 right로 지정해준 다음 중간으로 오면서 left가 right 보다 커지는 순간 반복문을 그만 돌게 한다.
2. 유사 회문 같은 경우 왼쪽에서 두번째 글자와 끝 글자를 비교해보거나 첫글자와 뒤에서 두번째 글자를 비교해봄으로써 계속 진행해준다.'''