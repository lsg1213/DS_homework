class ArrayQueue:
    DEFUALT_CAPACITY = 10
    def __init__(self):
        self._data = [None]*ArrayQueue.DEFUALT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        return self._data[self._front]

    def enqueue(self, v):
        if len(self._data) == self._size:
            self._data = self._resize(len(self._data) * 2)

        self._data[self._front + self._size % len(self._data)] = v
        self._size += 1
    
    def dequeue(self):
        
        a = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        self._size -= 1
        if len(self._data) // 2 >= self._size:
            self._data = self._resize(len(self._data) // 2)
            self._front = 0
        return a
        
    def _resize(self, c):
        tmp = [None] * c
        for i in range(self._size):
            tmp[i] = self._data[i + self._front % len(self._data)]
        
        return tmp


if __name__ == "__main__":
    a = ArrayQueue()
    print(a._data)
    for i in range(11):
        a.enqueue(i)
        print(a._data)
    for i in range(11):
        print(a.dequeue())
        print(a._data)