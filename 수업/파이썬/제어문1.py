# def greeting(name, age):
#     print(f'안녕, {name}, {age}!!')

# greeting('Alice', 25)
# greeting(25, 'Alice')
# greeting(age=25, name='Alice')

########################################################

# print('hi', 'aaa', 'bbb', 'ccc')
# print('hi', 'aaa', 'bbb')

# def calculate_sum(*args): #개수가 정해지지 않은 인자를 받음
#     print(args) #튜플로 들어감

# calculate_sum(1, 2, 3, 4, 5)

########################################################

# def print_info(**kwargs): #개수가 정해지지 않은 키워드를 받음
#     print(kwargs) #딕셔너리로 들어감

# print_info(name='Eve', age=30, address='korea')

########################################################

# def fac(n):
#     if n == 0:
#         return 1
    
#     return n * fac(n-1)

# result = fac(5)
# print(result)

########################################################

# names = ['Alice', 'Bob', 'Dave']
# ages = [10, 20, 30]
# cities = ['New York', 'London', 'seoul']

# for names, ages, cities in zip(names, ages, cities):
#     print(names, ages, cities, sep=' ')

########################################################

# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, numbers)) # map + lamda
# print(result)

########################################################

# print(0 or 3)
# print(1 or 2)
# print(3 and 5)
# print(0 and 4)

# lst = [1, 2, 3, 4, 5]

# for i in range(10):
#     if i < len(lst):
#         if lst[i] % 2 == 0:
#             print('짝수')

# for i in range(10):
#     if i < len(lst) and lst[i] % 2 == 0:
#         print('짝수')

########################################################

lst = [0] * 5
print(lst)

lst = [[0] * 4] * 4 # 이렇게 만들면 안된다.
lst[0][1] = 100

print(lst)

lst = [[0] * 4 for _ in range(4)]
print(lst)

lst[0][1] = 100

print(lst)

########################################################

# lst = []
# if lst: # 리스트가 비어있지 않으면
#     print(lst[0])

# if not lst: # 리스트가 비어 있으면
#     print('none')