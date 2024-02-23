# d = {
#     '국어' : 100,
#     '수학' : 80,
#     '영어' : 90,
# }
#
# print(d['영어'])
# d['과학'] = 77
# print(d['과학'])

# 최빈수
# 5 4 4 7 5 1 3 2 4 5
# dic = dict()
#
# for num in range(1, 11) :
#     dic[num] = 0
#
# numbers = list(map(int, input().split()))
#
# for number in numbers :
#     dic[number] += 1
#
# result = 0
# count = 0
#
# for el in dic :
#     if dic[el] >= count :
#         count = dic[el]
#         result = el
# print(result)



# 5 7 3 7 5 1 3 7 4 5
# 숫자를 입력 받으면, 리스트의 해당 인덱스의 값을 1 증가 시킨다.

data = list(map(int, input().split()))
counts = [0] * 101

for n in range(len(data)) :
    counts[data[n]] += 1

print(counts)

# count 내에서 최대값과 인덱스가 필요합니다.
max_num = 0
for i in range(1, 101) :
    if counts[i] >= counts[max_num] :
        max_num = i

print(max_num)
