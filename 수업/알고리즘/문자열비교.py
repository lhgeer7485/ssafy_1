T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    index_1 = 0

    is_flag = False

    while True:

        for x in range(len(str2)):
            if str1[index_1] == str2[x]:
                index_1 += 1
                is_flag = True
            else:
                is_flag = False
                index_1 = 0

            if index_1 >= len(str1) and is_flag:
                break

            if x == len(str2) - 1 and index_1 < len(str1):
                is_flag = False
                break
        break

    if is_flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

        
'''
1
qw
qrdq
'''
