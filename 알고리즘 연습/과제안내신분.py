std = [x for x in range(1, 31)]

for a in range(28):
    num = int(input())
    std.remove(num)

print(std[0])
print(std[1])