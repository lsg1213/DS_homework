class Empty(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class Parenthesis(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class Node:
    def __init__(self, data, depth, left = None, right = None, parent = None):
        self._parent = parent
        self._left = left
        self._right = right
        self._data = data
        self._depth = depth

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

    def changeParent(self, parent):
        self._parent = parent


class binTree(Node):
    def __init__(self):
        self._data = None
        self._size = 1
        self.equation = ''
        self.tracingDepth = 0
        self.height = 0

    def __len__(self):
        return self._size

    def get_root(self):
        return self._data

    def print_tree(self):    #LRC post-order
        self.__tracingLRC(self.get_root())

    def __tracingLRC(self,center):
        if center.getLeft() != None:
            self.__tracingLRC(center.getLeft())
        if center.getRight() != None:
            self.__tracingLRC(center.getRight())

        print('{} '.format(center.getData()),end='')

    def putData(self, equation):
        self.parenthsisCheck(equation)
        equation = self.postfix(equation)
        self._data = Node(equation.pop(), 0)
        self.makeNode(equation)
    
    def makeNode(self, equation):
        s = ArrayStack()
        for i in equation:
            if not i.isdigit():
                center = Node(i, None)
                right = s.pop()
                if type(right) != Node:
                    right = Node(right, None, parent=center)
                else:
                    right.changeParent(center)
                left = s.pop()
                if type(left) != Node:
                    left = Node(left, None, parent=Node)
                else:
                    left.changeParent(center)
                center.addRight(right)
                center.addLeft(left)
                s.push(center)
            else:
                s.push(i)
        self.get_root().addLeft(center)
        center.changeParent(self.get_root())
        self.get_root().addRight(Node(s.pop(),None,parent=self.get_root()))
        

        # if len(equation) == 0:
        #     return
        # if center._data.isdigit():
        #     return
        # else:
        #     t = equation.pop()
        #     if center.getRight() == None:
        #         center.addRight(Node(t,center._depth+1,parent=center))
        #         self.makeNode(equation,center.getRight())
        #         if self.height < center._depth + 1:
        #             self.height = center._depth + 1
        #     elif center.getLeft() == None:
        #         center.addRight(Node(t,center._depth+1,parent=center))
        #         self.makeNode(equation,center.getLeft())
        #         if self.height < center._depth + 1:
        #             self.height = center._depth + 1

    def parenthsisCheck(self, equation):
        s = ArrayStack()
        tmp = []
        #괄호 여닫기 처리
        for i in equation:
            if i == '(' or i == ')':
                s.push(i)

        if len(s) % 2 == 1:
            raise Parenthesis('number of parenthsis is odd!')

        for i in range(len(s) // 2):
            tmp.append(s.pop())
        for i in range(len(s) // 2):
            t = s.pop()
            if not (t == '(' and tmp[i] == ')'):
                raise Parenthesis('Wrong equation!')

    def priority(self, arg):
        if arg == '*' or arg == '/':
            return 5
        elif arg == '+' or arg == '-':
            return 3

    def postfix(self, equation):
        tmp = []
        s = ArrayStack()
        res = []
        #split equation
        for i in equation:
            if i.isdigit() and len(tmp) != 0:
                if tmp[-1].isdigit():
                    tmp.append(tmp.pop()+i)
                else:
                    tmp.append(i)
            else:
                tmp.append(i)
        
        for i in tmp:
            if i.isdigit():
                res.append(i)
                continue
            else:
                if i == '(':
                    s.push(i)
                elif i == ')':
                    while not s.is_empty():
                        v = s.pop()
                        if v != '(':
                            res.append(v)
                        else:
                            break
                else:
                    if not s.is_empty() and s.top() != '(':
                        if self.priority(s.top()) >= self.priority(i):
                            res.append(s.pop())
                            s.push(i)
                    else:
                        s.push(i)
        if not s.is_empty():
            res.append(s.pop())

        return res

    
if __name__ == "__main__":
    
    tree = binTree()
    tree.putData('(2+1)*(6+(7+4-1)-5)-3')
    tree.print_tree()