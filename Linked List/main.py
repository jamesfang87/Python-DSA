class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def add_any(self, middle_node, new_data):
        if middle_node is None:
            print('Node does not exist')
            return
        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def remove_any(self, removedata):
        head_node = self.head
        if head_node is not None:
            if head_node.data == removedata:
                self.head = head_node.next
                head_node = None
                return
        while head_node is not None:
            if head_node.data == removedata:
                break
            prev_node = head_node
            head_node = head_node.next
        if head_node is None:
            return
        prev_node.next = head_node.next
        head_node = None


list1 = singly_linked_list()
list1.add_first("Mon")
list1.add_first("Tue")
list1.add_first("Wed")
list1.add_first("Thu")
list1.display()
list1.remove_any("Thu")
list1.display()
