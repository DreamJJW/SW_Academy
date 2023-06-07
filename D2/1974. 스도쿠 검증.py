T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku = []
    answer = 1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    # 가로 판별
    for row in sudoku:
        if len(set(row)) != 9:
            answer = 0

    # 세로 판별
    for col in range(9):
        temp = []
        for j in range(9):
            temp.append(sudoku[j][col])
        if len(set(temp)) != 9:
            answer = 0

    # 3x3 영역 판별
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for x in range(3):
                for y in range(3):
                    temp.append(sudoku[x+i][y+j])
            if len(set(temp)) != 9:
                answer = 0

    print("#{0} {1}".format(test_case, answer))

