class Node:
    def __init__(self, data, left = None, right = None, parent = None):
        self._parent = parent
        self._left = left
        self._right = right
        self._data = data

    def getData(self):
        return self._data

    def getParent(self):
        return self._parent

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def addLeft(self, left):
        self._left = left

    def addRight(self, right):
        self._right = right


class binTree(Node):
    def __init__(self, data):
        self._data = Node(data)
        self._size = 1

    def __len__(self):
        return self._size

    def print_tree(self):    #LRC
        
    def evaluate(self):


if __name__ == "__main__":
    tree = binTree('A')