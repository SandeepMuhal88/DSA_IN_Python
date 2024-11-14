# Tree Making
# Binary Search Tree Making 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None
    
class Tree:
    def __init__(self):
        self.Root=None

    def insert(self,element):
        new_Node=Node(element)
        # Case First is Tree is empty
        if self.Root is None:
            self.Root=new_Node
            return
        
        # Case second is Tree is Not empty then :

        self.insertAgain(self.Root,element)
    
    # Definitation os InserAgain Method to use recursively
    # Then we assing curren =self.Root

    def insertAgain(self,current,data):
        if current.data<data:

            if current.right is None:
                current.data=None(data)
            else:
                self.insertAgain(current.right,data)
        elif current.data>data:
            if current.left is None:
                current.data=Node(data)
            else:
                self.insertAgain(current.left,data)
                
        #  # case 3: duplicate value will not be inserted
    
    def Search(self,element):
        self.SearchElement(self.Root,element)
    
    def SearchElement(self,current,data):
        # Case First is Tree is empty
        if current is None:
            print("Tree is Empty:(")
        elif current.data==data:
            print(f"{data} is found :)")
        else:
            if current.data>data:
                self.SearchElement(current.right,data)
            else:
                self.SearchElement(current.left,data)
    # Post Order and Inorder and Preorder
    # Properties 
    # Inorde(left,Right,Root)


    def Inorder(self):
        print("Inorder:",end=" ")
        self.inorder(self.Root)
    def inorder(self,current):
        if current:
                # Inorde(left,Right,Root)
            self.inorder(current.left)
            print(current.data,end=" ")
            self.inorder(current.Right)


    def Preorder(self):
        self.preorder(self.Root)
    def preorder(self,current):
        if current:
            # PreOrder(Root,left,Right)
            print(current.data,end=" ")
            self.preorder(current.left)
            self.preorder(current.right)
    
    def Postorder(self):
        self.postorder(self.Root)
    def postorder(self,current):
        if current:
            # Postorder(left,right,Root)
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data,end=" ")

obj=Tree()
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






# tree
# insert
# search
# treaversal (inorder,preorder,postorder,levelorder)
# delete