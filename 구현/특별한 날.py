m = int(input())
d = int(input())

if m == 2 and d == 18: print('Special')
elif m <= 2:
    if m == 2 and d >= 18: print('After')
    else: print('Before')
elif m >= 2:
    if m == 2 and d <= 18: print('Before')
    else: print('After')