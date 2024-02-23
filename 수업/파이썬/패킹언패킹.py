# a, *b = (1, 2, 3)

# print(a)
# print(b)

# lst = [1, 2, 3, 4, 5, 6]
# print(*lst) # 언패킹
# print(lst)

def my_sum(*args): # 여러개의 인자를 받는다 (패킹)
    print(sum(args))

my_sum(1, 2, 3)

lst = [1, 2, 3, 4, 5, 6]
my_sum(*lst) # 데이터를 풀어준다 (언패킹)

