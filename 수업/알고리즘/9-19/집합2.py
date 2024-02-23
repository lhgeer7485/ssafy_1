arr = [i for i in range(1, 4)]
path = [0] * 3

def backtracking(cnt, sum):
    if cnt == 3 and sum == 6:
        print(path)
        return
    if cnt == 3:
        return

    for num in arr:
        # if num in path:
        #     continue
        path[cnt] = num
        backtracking(cnt + 1, sum + num)
        #path[cnt] = 0

backtracking(0, 0)