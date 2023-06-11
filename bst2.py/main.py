class TreeEmptyError(Exception):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.data:
            p.left = self._insert(p.left, x)
        elif x > p.data:
            p.right = self._insert(p.right, x)
        else:
            print(f"{x} already present in the tree")
        return p

    def insert1(self, x):
        p = self.root
        parent = None
        while p is not None:
            parent = p
            if x < p.data:
                p = p.left
            elif x > p.data:
                p = p.right
            else:
                print(f"{x} already present in the tree")
                return

        temp = Node(x)

        if parent == None:
            self.root = temp
        elif x < parent.data:
            parent.left = temp
        else:
            parent.right = temp

    def search(self, x):
        return self._search(self.root, x) is not None

    def _search(self, p, x):
        if p is None:
            return None  # key not found
        if x < p.data:  # search in left subtree
            return self._search(p.left, x)
        if x > p.data:  # search in right subtree
            return self._search(p.right, x)
        return p  # key found

    def search1(self, x):
        p = self.root
        while p is not None:
            if x < p.data:
                p = p.left  # move to left child
            elif x > p.data:
                p = p.right  # move to right child
            else:  # x found
                return True
        return False

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, p, x):
        if p is None:
            print(f"{x} not found")
            return p

        if x < p.data:  # delete from left subtree
            p.left = self._delete(p.left, x)
        elif x > p.data:  # delete from right subtree
            p.right = self._delete(p.right, x)
        else:
            # key to be deleted is found
            if p.left is not None and p.right is not None:  # 2 children
                s = p.right
                while s.left is not None:
                    s = s.left
                p.data = s.data
                p.right = self._delete(p.right, s.data)

            else:  # 1 child or no child
                if p.left is not None:  # only left child
                    child = p.left
                else:  # only right child or no child
                    child = p.right
                p = child
            return p

    def delete1(self, x):
        p = self.root
        parent = None

        while p is not None:
            if x == p.data:
                break
            parent = p
            if x < p.data:
                p = p.left
            else:
                p = p.right

            if p == None:
                print(f"{x} not found")
                return

            # Case C: 2 children
            # Find inorder successor and its parent
            if p.left is not None and p.right is not None:
                ps = p
                s = p.right

                while s.left is not None:
                    ps = s
                    s = s.left
                p.data = s.data
                p = s
                parent = ps

            # Case B and Case A: 1 or no child
            if p.left is not None:  # node to be deleted has left child
                child = p.left
            else:  # node to be deleted has right child or no child
                child = p.right

            if parent == None:  # node to be deleted is self.root node
                self.root = child
            elif p == parent.left:  # node is left child of its parent
                parent.left = child
            else:
                parent.right = child

    # Iterative
    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.left is not None:
            p = p.left
        return p.data

    # Recursive
    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._min(self.root).data

    def _min(self, p):
        if p.left is None:
            return p
        return self._min(p.left)

    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.right is not None:
            p = p.right
        return p.data

    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._max(self.root).data

    def _max(self, p):
        if p.right is None:
            return p
        return self._max(p.right)

    def display(self):
        self._display(self.root, 0)
        print()

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.right, level + 1)
        print()

        for i in range(level):
            print("   ", end='')
        print(p.data)
        self._display(p.left, level + 1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, p):
        if p is None:
            return
        print(p.data, " ")
        self._preorder(p.left)
        self._preorder(p.right)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.left)
        print(p.data, " ")
        self._inorder(p.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.left)
        self._postorder(p.right)
        print(p.data, " ")

    def height(self):
        return self._height(self.root)

    def _height(self, p):
        if p is None:
            return 0

        heightL = self._height(p.left)
        heightR = self._height(p.right)

        if heightL > heightR:
            return 1 + heightL
        else:
            return 1 + heightR


########################################################

bst = BinarySearchTree()
bst.insert(60)
bst.insert(40)
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(50)
bst.insert(80)
bst.insert(70)
bst.insert(90)

while True:
    print("1.Display Tree")
    print("2.Search (Iterative)")
    print("3.Search (Recursive)")
    print("4.Insert a new node (Iterative)")
    print("5.Insert a new node (Recursive)")
    print("6.Delete a node (Iterative)")
    print("7.Delete a node (Recursive)")
    print("8.Find Minimum key (Iterative)")
    print("9.Find Minimum key (Recursive)")
    print("10.Find Maximum key (Iterative)")
    print("11.Find Maximum key (recursive)")
    print("12.Preorder Traversal")
    print("13.Inorder Traversal")
    print("14.Postorder Traversal")
    print("15.Height of tree")
    print("16.Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        bst.display()
    elif choice == 2:
        x = int(input("Enter the key to be searched: "))
        if bst.search1(x):
            print("Key found")
        else:
            print("Key not found")
    elif choice == 3:
        x = int(input("Enter the key to be searched: "))
        if bst.search(x):
            print("Key found")
        else:
            print("Key not found")
    elif choice == 4:
        x = int(input("Enter the key to be inserted: "))
        bst.insert1(x)
    elif choice == 5:
        x = int(input("Enter the key to be inserted: "))
        bst.insert(x)
    elif choice == 6:
        x = int(input("Enter the element to be deleted: "))
        bst.delete1(x)
    elif choice == 7:
        x = int(input("Enter the element to be deleted: "))
        bst.delete(x)
    elif choice == 8:
        print("Minimum key is ", bst.min1())
    elif choice == 9:
        print("Minimum key is ", bst.min2())
    elif choice == 10:
        print("Maxmimum key is ", bst.max1())
    elif choice == 11:
        print("Maxmimum key is ", bst.max2())
    elif choice == 12:
        bst.preorder()
    elif choice == 13:
        bst.inorder()
    elif choice == 14:
        bst.postorder()
    elif choice == 15:
        print("Height of tree is ", bst.height())
    elif choice == 16:
        break
    else:
        print("Wrong choice")
    print()

