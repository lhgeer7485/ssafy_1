T = int(input())
cnt = T

for tc in range(1, T + 1):
    st = input()
    is_break = False

    for a in range(len(st)-1):
        if is_break:
            break
        if st[a] != st[a+1]:
            for b in st[a+1:]:
                if st[a] == b:
                    cnt -= 1
                    is_break = True
                    break
print(cnt)