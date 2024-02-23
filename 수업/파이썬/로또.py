# 로또 번호 생성 프로그램

# import random

# lotto_nums = []

# while len(lotto_nums) < 6:
#     ran_num = random.randint(1, 45)
#     if ran_num in lotto_nums:
#         continue
#     lotto_nums.append(ran_num)

# lotto_nums.sort()

# print(lotto_nums)



######################################### 객체 지향
import random

class LottoNumberMaker:

    def __init__(self):
        self.lotto_nums = []
        pass

    def creat_number(self):
        while len(self.lotto_nums) < 6:
            ran_num = random.randint(1, 45)
            if ran_num in self.lotto_nums:
                continue
            self.lotto_nums.append(ran_num)

    def lotto_sort(self):
        self.lotto_nums.sort()

lotto = LottoNumberMaker()
lotto.creat_number()
lotto.lotto_sort()
print(lotto.lotto_nums)