st = input()

alp = [0] * 26

# A 65 / a 97 / Z 90 / z 122

for x in range(len(st)):
    num = ord(st[x])
    if num < 91:
        alp[num - 65] += 1
    else:
        alp[num - 97] += 1

max_alp = -1
count = 0
ind = 0

for x in alp:
    if max_alp < x:
        max_alp = x

for x in range(len(alp)):
    if max_alp == alp[x]:
        count += 1
        ind = x

if count > 1:
    print('?')

else:
    print(chr(ind + 65))