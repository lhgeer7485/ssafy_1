T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [list(map(int, input())) for _ in range(N)]
    pass_word = ''

    change = {'1011000': 0, '1001100': 1, '1100100': 2, '1011110': 3,
              '1100010': 4, '1000110': 5, '1111010': 6, '1101110': 7,
              '1110110': 8, '1101000': 9}
    code = ''

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                start = i
                break

    j = M - 1
    while j >= 6:
        code = ''
        for k in range(7):
            code += str(data[start][j - k])

        if code in change:
            pass_word += str(change[code])
            j -= 7
        else:
            j -= 1

        if len(pass_word) == 8:
            break

    new_pass = ''

    for x in reversed(range(len(pass_word))):
        new_pass += pass_word[x]

    n1 = 0
    n2 = 0

    for x in range(len(new_pass)):
        if x % 2 == 0:
            n1 += int(new_pass[x])
        else:
            n2 += int(new_pass[x])

    result = (n1 * 3) + n2

    if result % 10 != 0:
        result = 0
    else:
        result = n1 + n2
    
    print(f'#{tc} {result}')