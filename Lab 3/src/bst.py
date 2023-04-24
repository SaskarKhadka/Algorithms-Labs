from node import Node


class BinarySearchTree:

    def __init__(self) -> None:
        self.__root = None
        self.__size = 0

    def size(self):
        '''
        Returns the total number of nodes in the BST
        '''
        return self.__size

    def is_empty(self):
        '''
        Checks if the BST is empty
        Returns true if it is empty
        Else returns false
        '''
        return self.__root == None

    def add(self, key, value):
        '''
        Adds the given key-value to the BST if the key is unique
        Returns False if the given key already exists in the tree
        '''
        if self.search(key) == False:
            self.__root = self.__add(self.__root, key, value)
            self.__size += 1
            print(key, "added to BST")
        else:
            return False

    def __add(self, root, key, value):
        '''
        Helper function for add
        Recursively adds given key-value to the BST recursively
        '''
        if not root:
            root = Node(key, value)
        elif root.key > key:
            root.left = self.__add(root.left, key, value)
        elif root.key < key:
            root.right = self.__add(root.right, key, value)
        return root

    def search(self, key):
        '''
        Searches for the given key in the BST
        Returns the value of the key if it exists
        Else returns False
        '''
        return self.__search(self.__root, key)

    def __search(self, root, key):
        '''
        Helper function for search
        Recursively searches for the given key in BST
        '''
        if not root:
            return False
        elif root.key == key:
            return root.value
        elif root.key < key:
            return self.__search(root.right, key)
        else:
            return self.__search(root.left, key)

    def smallest(self):
        '''
        Finds the smallest key in the BST
        Returns the smallest key-value tuple if the tree is not empty
        Else returns False
        '''
        if not self.is_empty():
            return self.__smallest(self.__root)
        else:
            print("Cannot find the smallest in empty BST!!!")
            return False

    def __smallest(self, root):
        '''
        Helper function for smallest
        Recursively looks for the smallest value in the BST
        '''
        if not root.left:
            return (root.key, root.value)
        else:
            return self.__smallest(root.left)

    def largest(self):
        '''
        Finds the largest key in the BST
        Returns the largest key-value tuple if the tree is not empty
        Else returns False
        '''
        if not self.is_empty():
            return self.__largest(self.__root)
        else:
            print("Cannot find the largest in empty BST!!!")
            return False

    def __largest(self, root):
        '''
        Helper function for largest
        Recursively looks for the largest value in the BST
        '''
        if not root.right:
            return (root.key, root.value)
        else:
            return self.__largest(root.right)

    def remove(self, key):
        '''
        Removes the given key from the BST
        Returns False if the key doesnot exist
        '''
        result = self.__remove(self.__root, parent=None, key=key)
        if result != False:
            self.__size -= 1
            print(key, "removed from BST")
        else:
            return result

    def __remove(self, root, parent, key):
        '''
        Helper function for remove
        Recursively deletes the node with given key form the BST
        '''
        if root == None:
            return False
        elif root.key < key:
            return self.__remove(root.right, root, key)
        elif root.key > key:
            return self.__remove(root.left, root, key)
        else:
            # key found -> root
            # case 1 - no children
            if not root.left and not root.right:
                if not parent:
                    self.__root = None
                elif parent.left.key == key:
                    parent.left = None
                else:
                    parent.right = None
            # case 2 - left child only
            elif not root.right:
                if not parent:
                    self.__root = root.left
                elif parent.left.key == key:
                    parent.left = root.left
                else:
                    parent.right = root.left
            # case 3 - right child only
            elif not root.left:
                if not parent:
                    self.__root = root.right
                elif parent.left.key == key:
                    parent.left = root.right
                else:
                    parent.right = root.right
            # case 4 - both child
            else:
                # find largest from left child
                large = self.__largest(root.left)
                # copy the data from largest node to the node to be deleted
                root.key = large[0]
                root.value = large[1]
                # recursively delete the largest node in left child
                return self.__remove(root.left, root, root.key)

    def inorder_walk(self):
        '''
        Traverses the BST in inorder direction
        Returns a list nodes in the order in which they were visited
        '''
        nodes = []
        self.__inorder(self.__root, nodes)
        return nodes

    def __inorder(self, root, nodes):
        '''
        Helper function for inorder_walk
        Recursively performs inorder traversal through the BST
        '''
        if root:
            self.__inorder(root.left, nodes)
            nodes.append(root.key)
            self.__inorder(root.right, nodes)

    def preorder_walk(self):
        '''
        Traverses the BST in preorder direction
        Returns a list nodes in the order in which they were visited
        '''
        nodes = []
        self.__preorder(self.__root, nodes)
        return nodes

    def __preorder(self, root, nodes):
        '''
        Helper function for inorder_walk
        Recursively performs preorder traversal through the BST
        '''
        if root:
            nodes.append(root.key)
            self.__preorder(root.left, nodes)
            self.__preorder(root.right, nodes)

    def postorder_walk(self):
        '''
        Traverses the BST in postorder direction
        Returns a list nodes in the order in which they were visited
        '''
        nodes = []
        self.__postorder(self.__root, nodes)
        return nodes

    def __postorder(self, root, nodes):
        '''
        Helper function for inorder_walk
        Recursively performs postorder traversal through the BST
        '''
        if root:
            self.__postorder(root.left, nodes)
            self.__postorder(root.right, nodes)
            nodes.append(root.key)
