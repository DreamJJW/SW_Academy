t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    board = [[0] * n for j in range(n)]
    if n == 4:
        board[1][1], board[2][2] = 'W', 'W'
        board[1][2], board[2][1] = 'B', 'B'
    elif n == 6:
        board[2][2], board[3][3] = 'W', 'W'
        board[3][2], board[2][3] = 'B', 'B'
    else:
        board[3][3], board[4][4] = 'W', 'W'
        board[4][3], board[3][4] = 'B', 'B'

    for _ in range(m):
        x, y, color = map(int, input().split())
        if color == 1:
            board[x-1][y-1] = 'B'
        else:
            board[x-1][y-1] = 'W'



    print(board)