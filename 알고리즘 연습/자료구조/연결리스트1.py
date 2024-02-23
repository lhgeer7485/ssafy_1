################################################# 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
################################################# 헤드로 부터 노드 1 2 3까지 연결
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
################################################# 연결리스트 데이터 출력
# node = head
# while node:
#     print(node.data, end=" ")
#     node = node.next
################################################# 연결리스트 마지막에 추가
# node = head

# while node:
#     if node.next is None:
#         node.next = Node(4)
#         break
#     node = node.next
################################################# 연결리스트 처음에 추가
node = Node(0)
node.next = head
head = node
node = head
while node:
    print(node.data, end=" ")
    node = node.next