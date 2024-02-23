arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child_node):
        if not self.left:
            self.left = child_node
            return

        if not self.right:
            self.right = child_node
            return

        return

    def preorder(self):
        if self != None:
            print(self.value, end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()


nodes = [TreeNode(i) for i in range(0, 14)]

for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i + 1]
    nodes[parent_node].insert(nodes[child_node])

nodes[1].preorder()