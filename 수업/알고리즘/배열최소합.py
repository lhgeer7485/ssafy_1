def fnc(row, sum_data):
    global result_min
    # 시간을 줄이기 위해서 중간에서 계산중에 이미 행 데이터의 합의 값이 이미 최소값보다 커버리면
    # 더이상 재귀를 할 필요가 없으므로 중간에 멈춘다.
    if result_min < sum_data:
        return sum_data
    # 모든행의 합을 구했다면 합을 리턴
    if row == N:
        return sum_data
    # 열을 하나씩 증가해가면서 모든 경우를 확인해본다.
    for col in range(N):
        # 열이 중복이 안된다면
        if col_check[col] == 0:
            # 해당열은 사용을 못한다고 체크를 해주고
            col_check[col] += 1
            # 다음 행으로 넘어간다.
            # 현재까지의 합도 같이 넘겨준다.
            # 반환 값은 합을 받는다
            result = fnc(row + 1, sum_data + data[row][col])
            # 모든 계산 후 체크값을 다시 감소
            col_check[col] -= 1
            # 최소값과 행의 합을 체크해서 최고값을 갱신해나간다.
            if result_min > result:
                result_min = result
    # 최종 결과값인 최소값을 반환
    return result_min


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    # 열을 체크하는 리스트
    col_check = [0] * N
    # 행마다 하나씩 선택해서 더한 값을 저장하는 변수
    s = 0
    # 합의 최대값이 9*N을 넘을 수 없으므로 min을 9*N으로 초기화
    result_min = 9 * N

    print(f'#{tc} {fnc(0, s)}')
