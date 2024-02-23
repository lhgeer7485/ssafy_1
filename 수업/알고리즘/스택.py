# def stack_push(item):
#     global top

#     if top == SIZE:
#         print('overflow')
#     else:
#         top += 1
#         stack[top] = item

# def stack_pop():
#     global top
    
#     if top < 0:
#         print('underflow')
#     else:
#         stack.pop(top)
#         top -= 1



# SIZE = 10
# stack = [0] * SIZE
# top = -1

# stack_push(20)

# print(stack[top])


class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.s = [None] * max_size
        self.top = -1

    def pop(self):
        result = self.s[self.top]
        self.top -= 1
        return result

    def push(self, data):
        self.top += 1
        self.s[self.top] = data

    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def is_full(self):
        if self.top == self.max_size - 1:
            return True
        return False