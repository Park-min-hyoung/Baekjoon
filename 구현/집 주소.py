while True:
    num = input()
    if num == '0':
        break

    width = 0
    for i in range(len(num)):
        if num[i] == '1':
            width += 2
        elif num[i] == '0':
            width += 4
        else:
            width += 3
    width += (len(num) + 1)
    print(width)

'''
문제
1. 각 숫자 사이에는 1cm의 여백이 있어야 한다
2. 1은 2cm의 너비를 차지해야 한다. 0은 4cm의 너비를 차지, 나머지 숫자는 모두 3cm의 너비를 차지
3. 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야 한다.

입출력
1. 1 <= 숫자 범위 <= 9999
2. 0이 들어오기 전까지 계속해서 줄 단위로 주어진다(마지막 0은 처리x)
'''