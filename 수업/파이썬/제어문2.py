####################################################### if문

# num = int(input('숫자를 입력하세요 : '))
# if num % 2: # if num % 2 == 1:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

####################################################### for문

# country = 'korea'
# for c in country:
#     print(c, end=' ')

# numbers = [4, 6, 10, -8, 5]
# numbers = list(map(lambda x: x * 2, numbers))
# print(numbers)

# outers = ['A', 'B']
# inners = ['C', 'D']
# for outer in outers:
#     for inner in inners:
#         print(outer, inner)

# elements = [['A', 'B'], ['C', 'D']]
# for element in elements:
#     for elem in element:
#         print(elem)

#######################################################

# 1~10 요소에서 홀수만 가지는 리스트 만들기
# new_list = [x for x in range(1, 11) if x % 2 == 1]
# print(new_list)

####################################################### enumerate

# 인덱스와 요소를 가지는 튜플을 만듦 
fruits = ['apple', 'banana', 'cheerry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')





