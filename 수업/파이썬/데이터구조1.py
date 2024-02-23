#####################################
# st = 'hello'
# print(st.capitalize())

# print(st.find('l'))
# print(st.index('l'))
# print(st.isupper())
# print(st.lower())
# print(st.isalpha())
#####################################
# text = 'hello world'
# new_text = text.replace('world', 'python')
# print(new_text)

# text = '       hello world      '
# new_text = text.strip() # 문자열의 앞과 끝의 공백 or 지정된 문자 제거
# print(new_text)
#####################################
# words = ['hello', 'world','python']
# text = '-'.join(words)
# print(text)
#####################################
# my_list = [1, 2, 3]
# my_list.insert(1, 20)
# print(my_list)

# my_list.remove(1) # 0이 아니고 첫번째임 햇갈리지 말자 !!!
# print(my_list)

# print(my_list.pop())
# print(my_list.pop(1))

# my_list = [10, 20, 30]
# print(my_list.index(10)) # 인자와 같은 값을 가지는 인덱스를 반환

# my_list = [1, 2, 2, 3, 3, 3]
# cnt = my_list.count(3)
# print(cnt)

# my_list = [3, 2, 1]
# my_list.sort()
# print(my_list)
# print(sorted(my_list)) # 반환이 있다, 대신 원본은 안바뀐다

# my_list.sort(reverse=True) # 내림차순
# print(my_list)

# my_list = [1, 3, 2, 8, 1, 9] # 리스트의 순서를 역순으로, 정렬 x
# my_list.reverse()
# print(my_list)

#####################################

# lst = [5, 4, 3, 2, 1]

# print(''.join((map(str, lst))))

#####################################

# lst = [1, 2, 3, 4, 5]
# lst.remove(2) # remove는 값을 찾아서 삭제
# print(lst)
# lst = [1, 2, 3, 4, 5]
# lst.pop(2) # pop은 인덱스를 찾아서 삭제
# print(lst)

#####################################

lst = [3, 5, 2, 11, 31, 6, 1]
print(lst.sort()) # 함수의 반환값이 없어서 None으로 나옴
print(lst)

# lst = [3, 5, 2, 11, 31, 6, 1]
# sorted(lst)
# print(lst) # 리스트 자체를 정렬하지 않는다
#print(sorted(lst))