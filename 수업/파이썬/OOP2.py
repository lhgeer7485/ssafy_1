################################################# 상속

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'안녕, {self.name}입니다.')


# class Professor(Person):
#     def __init__(self, name, age, department):
#         #Person.__init__(self, name, age) 비추천, 아래처럼 쓰자.
#         super().__init__(name, age)
#         self.dapartment = department


# class Student(Person):
#     def __init__(self, name, age, gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa


# p1 = Professor('박교수', 49, '컴공')
# s1 = Student('김학생', 20, 3.5)

# p1.talk()
# s1.talk()

################################################# 다중 상속

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greeting(self):
#         return f'안녕, {self.name}'
    
# class Mom(Person):
#     gene = 'XX'

#     def __init__(self, name):
#         super().__init__(name)

#     def swim(self):
#         return '엄마가 수영'
    
# class Dad(Person):
#     gene = 'XY'

#     def __init__(self, name):
#         super().__init__(name)

#     def walk(self):
#         return '아빠가 걷기'
    
# class FirstChild(Mom, Dad):
#     dad_gene = Dad.gene

#     def __init__(self, name):
#         ## super().__init__(name) 이걸 쓰면 mom의 이름을 받아온다
#         Dad.__init__(name) # Dad를 가져오고 싶으면 Dad가 두번째라 super().말고 Dad.

#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
    
# baby1 = FirstChild('아가')
# print(baby1.cry())
# print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene)
# print(baby1.greeting()) 

# print(FirstChild.mro())

################################################# 예외 처리

# try:
#     num = int(input('100으로 나눌 값을 입력: '))
#     print(100/num)
# except ValueError:
#     print('숫자를 입력하세요')
# except ZeroDivisionError:
#     print('0 아닌 수를 입력하세요')
# except:
#     print('에러 발생')

#################################################

