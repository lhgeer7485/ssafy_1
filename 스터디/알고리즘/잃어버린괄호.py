import re
data = input()

numbers = re.split('[+-]', data)
oper = re.split('[0123456789]+', data)

print(numbers)
print(oper)