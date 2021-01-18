n = int(input())

for i in range(n):
    a = float(input())
    sale = round(a * 0.8, 2)

    print('$%.2f' %sale)