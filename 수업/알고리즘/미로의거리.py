def fnc(point_i, point_j):
    #  상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 시작지점을 큐에 추가
    queue.append((point_i, point_j))
    # 시작지점의 방문정보를 업데이트
    visited[point_i][point_j] = 1
    # 빈 큐가 아닐때까지 반복
    while queue:
        # 큐에서 pop을 해서 좌표를 가져온다.
        point_i, point_j = queue.pop(0)
        # 만약에 현재 좌표가 도착지점이라면
        if data[point_i][point_j] == '2':
            # 출발점과 도착점 사이의 거리를 출력하는것이기 때문에 -2를 한다.
            return visited[point_i][point_j] - 2
        # 상 하 좌 우 만큼 탐색하기 위해 델타 사용
        for d in range(4):
            ni = point_i + di[d]
            nj = point_j + dj[d]
            # 2차원 배열의 범위를 넘지 않는다면
            if 0 <= ni < N and 0 <= nj < N:
                # 이동하는 곳이 벽이 아니고 방문했던 곳이 아니라면
                if data[ni][nj] != '1' and visited[ni][nj] == 0:
                    # 이동좌표를 큐에 추가하고
                    queue.append((ni, nj))
                    # 이동좌표의 방문정보를 업데이트 해준다.
                    visited[ni][nj] = visited[point_i][point_j] + 1
    # 반복문안에서 리턴을 안했다는것은 도착점을 찾지 못했다는 것이므로 0을 리턴
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [input() for _ in range(N)]
    # 3부터 시작하기 위해 3의 좌표를 찾는다.
    for i in range(N):
        for j in range(N):
            if data[i][j] == '3':
                start_i = i
                start_j = j

    queue = []
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {fnc(start_i, start_j)}')
