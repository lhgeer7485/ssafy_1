# # 클래스 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'
    
#     # 메서드
#     def __init__(self, name):
#         self.name = name
        
#     def singing(self):
#         return f'{self.name}가 노래합니다.'

# # 인스턴스 생성
# singer1 = Person('iu')
# singer2 = Person('bts')

# # 메서드 호출
# print(singer1.singing())
# print(singer2.singing())

# # 속성(변수) 사용
# print(singer1.blood_color)
# print(singer2.blood_color)

##########################################################

# class Person:
#     name = 'unknown'

#     # 인스턴스 메서드
#     def talk(self):
#         print(self.name)

# p1 = Person()
# p1.talk()

# p2 = Person()
# p2.talk()
# p2.name = 'Kim'
# p2.talk()

# print(Person.name)
# print(p1.name)
# print(p2.name)

########################################################## 클래스메서드 (클래스가 사용)

# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

#     @classmethod
#     def num_of_population(cls):
#         print(f'인구수는 {cls.count}입니다.')

# p1 = Person('iu')
# p2 = Person('bts')

# p1.num_of_population()
# Person.num_of_population()

########################################################## 스태틱메서드 (클래스가 사용)

class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
    
text = 'hello world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)

capitalize_text = StringUtils.capitalize_string(text)
print(capitalize_text)