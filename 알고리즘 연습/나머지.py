numbers = []

for x in range(10):
    num = int(input())
    num %= 42
    numbers.append(num)

set_numbers = set(numbers)

print(len(set_numbers))
