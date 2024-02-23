#################################### set 메서드

# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)

# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)

# my_set = {1, 2, 3}
# my_set.remove(2) # 요소를 제거 (인덱스 아님, set라서 당연)
# print(my_set)
# my_set.discard(10) # 없는것을 제거해도 에러가 나지 않는다.
# print(my_set)
# print(my_set.discard(10))

# my_set = {1, 2, 3}
# element = my_set.pop() # 해시테이블상에서 주소값이 가장 빠른 값을 삭제
# print(element)
# print(my_set)

# my_set = {1, 2, 3}
# my_set.update([4, 5]) # 하나 추가는 불가, 연속성을 가지는 데이터를 추가할때 사용
# print(my_set)

# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}
# print(set1.difference(set2))
# print(set1.intersection(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
# print(set1.union(set2))

#################################### dictionary 메서드

# person = {'name' : 'Alice', 'age' : 25}
# print(person.get('name')) # person['name']과 결과가 같다.
# print(person.get('country')) # 하지만 없는 키값의 경우 에러가 안나오고 None이 나온다.
# print(person.get('country', 'Unknown')) # 없을때 나올 값을 정해줄 수 있다.

# person = {'name' : 'Alice', 'age' : 25}
# print(person.keys())
# for x in person.keys():
#     print(x)

# person = {'name' : 'Alice', 'age' : 25}    
# print(person.values())
# for x in person.values():
#     print(x)

# person = {'name' : 'Alice', 'age' : 25}
# print(person.items()) # 튜플로 키와 벨류가 나온다.
# for key, value in person.items():
#     print(key, value)

# person = {'name' : 'Alice', 'age' : 25}
# print(person.pop('name'))
# print(person.items())
# print(person.pop('country', 'country 키는 없어요')) # 없는키면 에러가 나오지만 대신 출력할 default 반환 가능.

# person = {'name' : 'Alice', 'age' : 25} 
# print(person.setdefault('country', 'korea')) # get과 똑같이 해당 키의 벨류를 가져오지만, 해당 키가 없을경우 키를 추가하고 default에 적은 값을 벨류에 넣는다. 그리고 default 값을 반환까지 한다 !
# print(person.items())

# person = {'name' : 'Alice', 'age' : 25}
# other_person = {'name' : 'Jane', 'gender' : 'Female'}
# person.update(other_person) # 추가하지만 키가 중복일 경우 계속 덮어 씌운다.
# print(person)
# person.update(age=50)
# print(person)

#################################### 혈액형 인원수 제거
# 결과 >> {'A' : 3, 'B' : 3, 'O' : 3, 'AB' : 3}

#### 1) []

# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# new_dict = {}
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     if blood_type in new_dict:
#         # 기존 키의 값을 +1 증가
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면 (처음 설정되는 키)
#     else :
#         new_dict[blood_type] = 1
# print(new_dict)

#### 2) .get[]

# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# new_dict = {}
# for blood_type in blood_types:
#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
# print(new_dict)


#### 3) .setdefault()

# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# new_dict = {}
# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0)
#     new_dict[blood_type] += 1
# print(new_dict)

#################################### 얕은 복사

# a = [1, 2, 3]
# b = a[:]
# b[0] = 100
# print(a, b)
# c = a.copy()
# c[0] = 100
# print(a, c)

#################################### 얕은 복사의 한계 (중요)

# a = [1, 2, [1, 2]]
# b = a[:]
# b[2][0] = 999
# print(a, b)

# a = [1, 2, [1, 2]]
# c = a.copy()
# c[2][0] = 999
# print(a, c) # 겉의 리스트만 복사되고 안에 있는 리스트는 복사가 안됨

#################################### 깊은 복사

# import copy
# original_list = [1, 2, [1, 2]]
# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[2][0] = 999
# print(original_list, deep_copied_list)