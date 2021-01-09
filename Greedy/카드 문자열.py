n = int(input())
for i in range(n):
    num = int(input())
    alpha = list(input().split())

    realpha = []
    left = ord(alpha[0])
    for j in range(num):
        if j == 0: realpha.append(alpha[j])
        else:
            if ord(alpha[j]) <= left:
                left = ord(alpha[j])
                realpha.insert(0, alpha[j])
            else:
                realpha.append(alpha[j])
    print(''.join(realpha))


