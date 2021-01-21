score = list(map(int, input().split()))

if sum(score) >= 100:
    print("OK")
else:
    mi = min(score)
    if mi == score[0]: print("Soongsil")
    elif mi == score[1]: print("Korea")
    elif mi == score[2]: print("Hanyang")