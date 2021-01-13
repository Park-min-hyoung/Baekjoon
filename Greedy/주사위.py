n = int(input())
dice = list(map(int, input().split()))
sum = 0
dice_sum = []

if n == 1:
    dice.sort()
    for i in range(5):
        sum += dice[i]
else:
    dice_sum.append(min(dice[0], dice[5]))
    dice_sum.append(min(dice[1], dice[4]))
    dice_sum.append(min(dice[2], dice[3]))
    dice_sum.sort()

    one = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    two = 4 * (n - 1) + 4 * (n - 2)
    three = 4

    sum += dice_sum[0] * one
    sum += (dice_sum[0] + dice_sum[1]) * two
    sum += (dice_sum[0] + dice_sum[1] + dice_sum[2]) * three

print(sum)

# 틀렸음
'''나의 해결 : 어느 정도 접근은 했지만 접근 방법도 달랐고 마주보는 면을 처리하는 방법도 생각 해내지 못했다.'''
'''해결 아이디어
1. 주사위가 1개일때는 그냥 밑면을 가장큰걸로 하고 나머지 5개를 더하면 끝이다.
2. 주사위가 8개(n = 2)이상일 때 인접한 면중 어떤 면을 사용할 것인지 부터 정해줌으로써 3개의 면을 배열에 담아두고 오름차순으로 정렬한다.
3. 면이 1개 필요한 주사위 개수, 2개가 필요한 주사위 개수, 3개가 필요한 주사위 개수를 변수에 저장한다음 계산해준다.
4. 어렵다 많이 어렵고 쉽지 않을 것 같지만 계속 해야지!!!'''