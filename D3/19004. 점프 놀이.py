t = int(input())
for test_case in range(t):
    board = []
    n, k = map(int, input().split())
    for _ in range(n):
        board.append(list(map(int, input().split())))

    start = [0, 0]
    start_num = 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == start_num:
                if board[i+1][j-1] == start_num+1 or board[i+1][j+1] == start_num+1\
                        or board[i][j-1] == start_num+1 or board[i+1][j] == start_num+1:
                    dis = ()

