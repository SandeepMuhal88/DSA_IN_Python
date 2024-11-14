class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        newNode = Node(element)
        # case 1: Tree is empty
        if self.root is None:
            self.root = newNode
            return

        # case 2 : Tree is not empty

        self.insertAgain(self.root, element)

    def insertAgain(self, current, data):

        if current.data < data:
            if current.right is None:
                current.right = Node(data)
            else:
                self.insertAgain(current.right, data)

        elif current.data > data:
            if current.left is None:
                current.left = Node(data)
            else:
                self.insertAgain(current.left, data)

        # case 3: duplicate value will not be inserted

    # def info(self):
    #     print(self.root.left.right.data)

    def serach(self, element):
        self.searchElement(self.root, element)

    def searchElement(self, current, data):
        # current = Tree
        # data = 8

        # case 1: if data not found then current will execute
        if current is None:
            print(f"{data} Not found")

        # case 2: root = data

        elif current.data == data:
            print(f"{data} found")

        else:
            if current.data < data:
                self.searchElement(current.right, data)
            else:
                self.searchElement(current.left, data)

    def inorder(self):
        print("Inorder : ", end=" ")
        self.Inorder(self.root)
        print()

    def Inorder(self, current):
        if current:
            self.Inorder(current.left)
            print(current.data, end=" ")
            self.Inorder(current.right)

    def preorder(self):
        print("Preorder :", end=" ")
        self.Preorder(self.root)
        print()

    def Preorder(self, current):
        if current:
            print(current.data, end=" ")
            self.Preorder(current.left)
            self.Preorder(current.right)

    def postorder(self):
        print("Postorder :", end=" ")
        self.Postorder(self.root)
        print()

    def Postorder(self, current):
        if current:
            self.Postorder(current.left)
            self.Postorder(current.right)
            print(current.data, end=" ")

    def delete(self, element):
        # case1 : tree is empty
        if self.root is None:
            print("Tree is empty ")
            return
        # case 2 : tree is Not empty
        self.delete_element(self.root, element)

    def delete_element(self, current, data):
        if current is None:
            return current
        elif current.data < data:
            current.right = self.delete_element(current.right, data)
        elif current.data > data:
            current.left = self.delete_element(current.left, data)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            temp = self.minimum(current.right)
            current.data = temp.data
            current.right = self.delete_element(current.right, temp.data)
        return current

    def minimum(self, current):
        while current.left:
            current = current.left
        return current


obj = Tree()
# 9,13,7,3,8,14,18,2
obj.insert(9)
obj.insert(13)
obj.insert(7)
obj.insert(3)
obj.insert(8)
obj.insert(14)
obj.insert(18)
obj.insert(2)
obj.inorder()
obj.preorder()
obj.postorder()
# obj.info()


# tree
# insert
# search
# treaversal (inorder,preorder,postorder,levelorder)
# delete


# avl tree