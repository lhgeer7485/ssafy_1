lst = [1,2,3,4,5,6,7,8,9,10]


############################### 함수버전
# def fnc(x):
#     return x * 2

# new_lst = list(map(fnc, lst))

# print(new_lst)

############################### 람다버전

# new_lst = list(map(lambda x : x * 2, lst))
# print(new_lst)


lst = [
        {'name' : '이해건', 'age' : 29, 'city' : '대구'},
        {'name' : '김상우', 'age' : 21, 'city' : '서울'},
        {'name' : '김동현', 'age' : 41, 'city' : '인천'},
        {'name' : '정지수', 'age' : 19, 'city' : '광주'},
        ]

new_lst = list(map(lambda dict: {'name' : dict['name'], 'age' : dict['age']}, lst))

print(new_lst)