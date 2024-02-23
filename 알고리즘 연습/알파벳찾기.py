S = input()

data = [-1] * 26
# a (97) ~ z (122)

for x in reversed(range(len(S))):
    data[ord(S[x])-97] = x

print(*data)