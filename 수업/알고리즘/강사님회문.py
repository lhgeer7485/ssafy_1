# is_find = False
# for i in range(M//2):
#     if data[i] != data[M-i-1]:
#         break

# else:
#     is_find = True


txt = 'ABABCCBACB'
N = len(txt)
M = 6
is_find = False

for i in range(N - M + 1):
    for j in range(M//2):
        if txt[i+j] != txt[i+M-1-j]:
            break
    else:
        is_find = True