data = list(map(int, input().split()))

# counts = 0

# for x in range(len(data)):
#     if data[x] == x + 1:
#         counts += 1

data_1 = [x for x in range(1, 9)]
data_2 = [x for x in reversed(range(1, 9))]

if data == data_1:
    print('ascending')
elif data == data_2:
    print('descending')
else:
    print('mixed')