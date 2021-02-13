class SortedList:
    def __init__(self, ascending_check):
        self.headNode = None
        self.currentNode = None
        self.length = 0
        self.ascending_check = ascending_check

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        
    def insert(self, newNode):
        self.length += 1
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return
        if self.ascending_check == '1':
            # Check if it is going to be new head
            if newNode < self.headNode:
                self.__appendToHead(newNode)
                return
            # Check it is going to be inserted
            # between any pair of Nodes (left, right)
            leftNode = self.headNode
            rightNode = self.headNode.nextNode
            while rightNode != None:
                if newNode < rightNode:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return
                leftNode = rightNode
                rightNode = rightNode.nextNode
            # Once we reach here it must be added at the tail
            leftNode.nextNode = newNode
        else:
            # Check if it is going to be new head
            if newNode > self.headNode:
                self.__appendToHead(newNode)
                return
            # Check it is going to be inserted
            # between any pair of Nodes (left, right)
            leftNode = self.headNode
            rightNode = self.headNode.nextNode
            while rightNode != None:
                if newNode > rightNode:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return
                leftNode = rightNode
                rightNode = rightNode.nextNode
            # Once we reach here it must be added at the tail
            leftNode.nextNode = newNode

    # overloading operator

    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (',' + node.__str__())
                node= node.nextNode
        return output

    def __len__(self):
        return self.length
    
    def __getitem__(self, key):
        node = self.headNode
        for i in range(key):
            node = node.nextNode
        return node

        