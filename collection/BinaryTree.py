class BinaryTree:
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def get_left_tree(self):
        return self.leftTree

    def get_right_tree(self):
        return self.rightTree

    def insert_left(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree

    def insert_right(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree