for i in range(3):
    ep = list(map(int, input().split()))

    if ep[5] - ep[2] >= 0:
        s = ep[5] - ep[2]
    else:
        s = ep[5] - ep[2] + 60
        ep[4] -= 1

    if ep[4] - ep[1] >= 0:
        m = ep[4] - ep[1]
    else:
        m = ep[4] - ep[1] + 60
        ep[3] -= 1

    h = ep[3] - ep[0]

    print(h, m, s)

'''깔끔하게 푸는 방법
for i in range(3):
    fh, fm, fs, lh, lm, ls = map(int, input().split())

    first = (fm * 60) + (fh * 3600) + fs
    last = (lm * 60) + (lh * 3600) + ls
    time = last - first

    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60

    print(h, s, m)
'''