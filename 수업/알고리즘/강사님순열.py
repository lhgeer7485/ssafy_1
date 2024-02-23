# def f(i, N, K):
#     if i == K:
#         print(result)
#         return

#     for j in range(N):
#         if not used[j]:
#             result[i] = card[j]
#             used[j] = 1
#             f(i + 1, N, K)
#             used[j] = 0


# def f(i):
#     if i == K:
#         print(result)
#         return

#     for j in range(N):
#         result[i] = card[j]

#         f(i + 1)

# N = 6
# K = 2
# #card = [1, 2, 3, 4, 5]
# card = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
# used = [0] * N
# result = [0] * K
# f(0)

# data = [1, 2, 3, 4]

# bit = [0] * 4
        




# def f2(i):
#     if i == 4:
#         result = []
#         for x in range(len(bit)):
#             if bit[x]:
#                 result.append(data[x])
#         print(result)
#         return

#     bit[i] = 1
#     f2(i + 1)
#     bit[i] = 0
#     f2(i + 1)


# def f3():
#     a = [1, 2, 3, 4]
#     N = 4
#     for i in range(1, 1 << (N - 1)):
#         result1 = []
#         result2 = []
#         for j in range(N):
#             if i & (1 << j):
#                 result1.append(a[j])
#             else:
#                 result2.append(a[j])
#         print(result1, result2)




# f2(0)

#f3()





def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A = [1, 2, 3]
N = len(A)
R = 2
comb = [0] * R
nCr(N, R, 0)
