# def f(i, N):
#     if i == N:
#         #print(bit, end=' ')
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#                 print(A[j], end=' ')
#         #print()
#         print(f': {s}')
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, N)
#         bit[i] = 0
#         f(i + 1, N)
#         return


# N = 3
# A = [1, 2, 3]
# bit = [0] * N
# f(0, N)

###############################################

#s : i-1 원소까지 부분집합의 합

def f(i, N, s):
    if i == N:

        for j in range(N):
            if bit[j]:

                print(A[j], end=' ')
        print(f': {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N, s+A[i])
        bit[i] = 0
        f(i + 1, N, s)
        return


N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N, 0)

###############################################

# def f(i, N, s):
#     if i == N:
#         #print(bit, end=' ')
#         #s = 0
#         if s == 3:
#             print(bit)
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, N, s+A[i])
#         bit[i] = 0
#         f(i + 1, N, s)
#         return


# N = 3
# A = [1, 2, 3]
# bit = [0] * N
# f(0, N, 0)

###############################################

# def f(i, N, s, t):

#     if s == t:
#         print(bit)
#         return
#     elif i == N:
#         return
#     elif s > t:
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, N, s+A[i], t)
#         bit[i] = 0
#         f(i + 1, N, s, t)
#         return

# N = 10
# A = [i for i in range(1, N + 1)]
# bit = [0] * N
# cnt = 0
# t = 10
# f(0, N, 0, t)

###############################################

# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]

# A = [1, 2, 3 ]
# f(0, 3)