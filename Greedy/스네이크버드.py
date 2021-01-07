n, l = map(int, input().split())
apple = list(map(int, input().split()))
apple.sort()

for i in apple:
    if l >= i: l += 1
print(l)