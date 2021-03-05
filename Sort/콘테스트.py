def sum_score():
    data = []
    score = 0

    for i in range(10):
        data.append(int(input()))
    data.sort(reverse=True)

    for i in range(3):
        score += data[i]

    return score


y_score = sum_score()
k_score = sum_score()

print(y_score, k_score)