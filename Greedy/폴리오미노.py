board = input()

i = 0
while True:
    if i == len(board): break

    if board[i:i+4] == 'XXXX':
        i += 4
        board = board.replace('X', 'A', 4)
    elif board[i:i+2] == 'XX':
        i += 2
        board = board.replace('X', 'B', 2)
    elif board[i] == '.':
        i += 1
    else:
        board = -1
        break
print(board)

# 틀렸음
'''나의 해결 : 틀렸다'''
'''해결 아이디어
1. for문을 돌려 해당 인덱스 번호와 인덱스 번호 + 4까지의 값이 XXXX이면 AAAA로 바꿔주고 +2까지의 값이 XX이면 BB로 바꿔준다.
2. 해당사항이 없으면 -1'''