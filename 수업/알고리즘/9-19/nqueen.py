def nqueen(row):
    if row == N:
        for r in board:
            print(r)
        print('-----------------------------------')
        return

    for i in range(N):
        if not visited[i] and not dia1[row + i] and not dia2[row - i + N - 1]:
            board[row][i] = 1
            visited[i] = 1
            dia1[row+i] += 1
            dia2[row - i + N - 1] += 1

            nqueen(row + 1)

            board[row][i] = 0
            visited[i] = 0
            dia1[row + i] -= 1
            dia2[row - i + N - 1] -= 1

N = 4
board = [[0] * N for _ in range(N)]
visited = [0] * N
dia1 = [0] * (2 * N - 1)
dia2 = [0] * (2 * N - 1)
nqueen(0)
