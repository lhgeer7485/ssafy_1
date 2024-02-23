import math

a = 3.2 - 3.1
b = 1.2 - 1.1

print(2 / 3)
print(5 / 3)

print(math.isclose(a, b))

# 314 * 0.01
number = 314e-2
print(number)

#지수(제곱하는 횟수) 표현 10^
print(314e2) # 31400.0
###################################################
greeting = 'hi'
print(f'{greeting:^10}')
print(f'{greeting:>10}')
print(f'{greeting:<10}')
print(f'{3.141592:.4f}')

my_str = 'hello'

print(my_str[0:5:2]) #0~4까지 2칸씩 띄우기
print(my_str[::-1]) #문자열 뒤집기
###################################################
my_tuple = ()
my_tuple = (1,)
print(my_tuple)

x, y = (10, 20)
print(x)
print(y)
###################################################
my_dict_1 = {'key1' : 'value1', 'key2' : 'value2'}
my_dict_2 = {'int' : 12, 'list' : [1, 2, 3]}

print(my_dict_1)
print(my_dict_2)
print(my_dict_1['key1'])
print(my_dict_2['list'])
###################################################
my_set_1 = set()
my_set_2 = {1, 4, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)
print(my_set_2)
print(my_set_3)

my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

#합집합
print(my_set_1 | my_set_2)

#차집합
print(my_set_1 - my_set_2)

#교집합
print(my_set_1 & my_set_2)
###################################################
lst_1 = [1, 2, 3]
lst_2 = lst_1 #주소값
lst_1[0] = 100

print(lst_1, lst_2)

lst_1 = [1, 2, 3]
lst_2 = lst_1[:]
lst_1[0] = 100

print(lst_1, lst_2)
###################################################


