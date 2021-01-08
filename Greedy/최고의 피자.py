top = int(input())
price = list(map(int, input().split()))
dow_k = int(input())

top_k = []
for i in range(top):
    top_k.append(int(input()))
top_k.sort(reverse=True)

top_ks = top_k[0]
temp = dow_k / price[0]
for i in range(len(top_k)):
    if temp <= (dow_k + top_ks) / (price[0] + (price[1] * (i + 1))):
        temp = (dow_k + top_ks) / (price[0] + (price[1] * (i + 1)))
        if i < len(top_k) - 1: top_ks += top_k[i + 1]
print('%.d' %temp)