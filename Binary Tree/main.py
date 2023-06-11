class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, e):
        new_node = Node(e, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def display(self):
        head_node = self.head
        while head_node:
            print(head_node.data, end = '-->')
            head_node = head_node.next
        print()


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def make_tree(self, e, left, right):
        self.root = TreeNode(e, left.root, right.root)
        left.root = None
        right.root = None

    def level_order(self):
        q = LinkedQueue()
        root_node = self.root
        print(root_node.data, end='--')
        q.enqueue(root_node)

        while not q.is_empty():
            node = q.dequeue()
            if node.left:
                print(node.left.data, end='--')
                q.enqueue(node.left)
            if node.right:
                print(node.right.data, end='--')
                q.enqueue(node.right)

    def inorder(self, root_node):
        if root_node:
            self.inorder(root_node.left)
            print(root_node.data, end='--')
            self.inorder(root_node.right)

    def preorder(self, root_node):
        if root_node:
            print(root_node.data, end='--')
            self.preorder(root_node.left)
            self.preorder(root_node.right)

    def postorder(self, root_node):
        if root_node:
            self.postorder(root_node.left)
            self.postorder(root_node.right)
            print(root_node.data, end='--')