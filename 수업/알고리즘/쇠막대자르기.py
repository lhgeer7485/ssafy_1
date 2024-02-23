T = int(input())

for tc in range(1, T + 1):
    data = input()
    # 쇠 막대기 수
    steal = 0
    # 절단한 쇠 막대기 수
    result = 0

    for x in range(len(data)):
        # ( 의 경우
        if data[x] == '(':
            # 다음 괄호가 )라서 레이저인 경우
            if data[x+1] == ')':
                # 현재 쇠 막대기의 수 만큼 절단한 쇠 막대기 수 증가
                result += steal
            # 레이저가 아닌 경우
            else:
                # 쇠 막대기 수 증가
                steal += 1
        # ) 면서 레이저가 아닌 경우
        elif data[x] == ')' and data[x-1] == ')':
            # 쇠 막대기 수 감소
            steal -= 1
            # 쇠 막대기가 하나 줄었으므로, 절단 되고 남은 부분을 result에 추가
            result += 1

    print(f'#{tc} {result}')