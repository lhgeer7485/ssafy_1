def stack_push(item):
    global top

    top += 1
    my_stack[top] = item

def stack_pop():
    global top

    my_stack.pop(top)
    top -= 1

T = int(input())

for tc in range(1, T + 1):

    data = input()

    SIZE = len(data)
    top = -1
    my_stack = [0] * SIZE
    # 반복문을 통과했는지 확인하는 변수
    is_result = True

    for x in data:
        # ( { 일 때
        if x == '(' or x == '{':
            if top >= SIZE:
                is_result = False
                break                
            # 스택에 추가
            stack_push(x)
        # ) 일 때
        elif x == ')':
            # 빈 스택이면 틀린것이니 종료            
            if top < 0:
                is_result = False
                break
            else:                
                # 스택의 탑이 ( 라면 pop
                if my_stack[top] == '(':
                    stack_pop()
                else:
                    is_result = False
                    break

        elif x == '}':
            # 빈 스택이면 틀린것이니 종료            
            if top < 0:
                is_result = False
                break
            else:                
                # 스택의 탑이 { 라면 pop
                if my_stack[top] == '{':
                    stack_pop()
                else:
                    is_result = False
                    break


    # 반복문은 통과했지만 스택에 괄호가 남아 있으면 틀린것    
    if is_result:
        if top >= 0:
            print(f'#{tc} 0')
        # 빈 스택이면 맞음
        else:
            print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')