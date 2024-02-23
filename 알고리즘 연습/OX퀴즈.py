N = int(input())

data = []



for x in range(N):
    data.append(input())




for a in range(N):
    plus = 0
    score = 0
    for x in data[a]:
        if x == 'O':
            score += 1 + plus
            plus += 1
        elif x == 'X':
            plus = 0

    print(score)