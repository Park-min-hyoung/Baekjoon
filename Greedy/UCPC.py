import sys
input = sys.stdin.readline

sen = input()
check_li = ["U", "C", "P", "C"]
check = True

for i in range(len(check_li)):
    if check_li[i] in sen:
        check = True
        index = sen.find(check_li[i])
        sen = sen[index + 1:]
    else:
        check = False
        break

if check == True: print("I love UCPC")
else: print("I hate UCPC")

# 틀렸음
'''나의 해결 : 출력이 제대로 나와서 문제가 없는지 알았는데 틀렸다'''
'''해결 아이디어
1. U,C,P,C를 배열에 준비하고 변수(check)를 통해 boolean 값 판별
2. 그냥 준비해둔 배열에 만족하는 값이 다 있으면 그만이므로 그 값을 찾을때마다 찾은 위치를 포함한 이전의 위치는 자르면 된다'''