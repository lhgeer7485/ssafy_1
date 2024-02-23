#
# print('Hello world!')
#
# num = 10
# st = 'Hello'
# flag = True
#
# name = '홍길동'
# # greeting = '안녕하세요 홍길동입니다.'
#
# greeting = f'안녕하세요 {name}입니다.'
#
# print(greeting)
#
# scores = [100, 90, 95]
#
# print(scores[-2])
# scores[1] = 99
# print(scores[-2])
#
# tScores = (100, 90, 95)
# print(tScores[2])
#
# 문자열 튜플은 immutable
# 리스트는 mutable
#
# myList = list(map(int, input().split()))
# print(myList)
#
# 파일로 읽어오기
#
# ----------------------------------------------------
# import sys
# sys.stdin = open('input.txt', 'r')
# # sys.stdout = open('ouput.txt', 'w')
# data = input().split(',')
# print(list(map(int, data)))

# num = list(map(int, input()))
# print(num)

# arr = [0] * 100
# print(arr)

# arr = [x for x in range(1, 101)]
# print(arr)
# ----------------------------------------------------

# arr = [0] * 10
# arr[2] = 500

arr = [100, 200, 300, 400, 500]
# for a in arr :
#     print(a)
# for i in range(5) :
#     print(i)
# for i in range(5) :
#     print(arr[i])
# for i in range(len((arr))) :
#     print(i)

for i in range(len(arr)) :
    if i % 2 == 0 :
        print(arr[i])

