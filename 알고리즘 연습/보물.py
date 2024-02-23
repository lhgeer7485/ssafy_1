N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# sorted_A = sorted(A)

# new_A = [-1] * N


# sorted_B = sorted(B)
# sorted_B.reverse()


# for sb in range(N):
#     for b in range(N):
#         if sorted_B[sb] == B[b]:
#             new_A[b] = sorted_A[sb]
#             break


# def fnc(A, B):
#     S = 0
#     for x in range(len(A)):
#         S += A[x] * B[x]
#     return S

# print(fnc(new_A, B))
#print('A ', A)
#print('B ', B)

S = 0
for x in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)