N, A, B = map(int, input().split())

count = 0

while A != B:
    A = (A + 1) // 2
    B = (B + 1) // 2
    count += 1

print(count)
