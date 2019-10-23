class ArrayStack:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.__len__() == 0

    def push(self, v):
        self._data.append(v)

    def top(self):
        return self._data[self.__len__() - 1]

    def pop(self):
        if self.is_empty():
            raise ValueError('empty stack')
        return self._data.pop()

if __name__ == "__main__":
    a = ArrayStack()
    print(a.is_empty())
    a.push('hi')
    print(a.top())
    print(a._data)
    print(a.pop())
    print(a._data)

True
hi
['hi']
hi
[]