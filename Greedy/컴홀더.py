men = int(input())
seat = input()
seatcf = []

while len(seat) != 0:
    if seat[0] == 'S':
        seatcf.append(seat[0])
        seat = seat[1:len(seat)]

    elif seat[0] == 'L':
        seatcf.append(seat[0] + seat[1])
        seat = seat[2:len(seat)]

d = 0
for i in range(0, len(seatcf) - 1):
    if seatcf[i] != seatcf[i + 1]: d = 1

if d == 0:
    if seatcf[0] == 'S': print(len(seatcf))
    elif seatcf[0] == 'LL': print(men // 2 + 1)
elif d == 1:
    print(len(seatcf) + 1)

# 맞았음
'''맞긴 맞았는데 구글의 소스가 너무 어이 없게 쉽게 나와서(https://s0ng.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B7%B8%EB%A6%AC%EB%94%94-%
EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%BB%B5%ED%99%80%EB%8D%94-2810%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python)'''