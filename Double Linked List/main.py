class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def add_first(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def add_any(self, prev_node, newdata):
        if prev_node is None:
            return
        new_node = Node(newdata)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def add_last(self, newdata):
        new_node = Node(newdata)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        return 

    def display(self, node):
        while (node is not None):
            print(node.data)
            node = node.next

###########################################

dlist1 = doubly_linked_list()
dlist1.add_first(12)
dlist1.add_last(9)
dlist1.add_first(8)
dlist1.add_first(62)
dlist1.add_last(45)
dlist1.display(dlist1.head)