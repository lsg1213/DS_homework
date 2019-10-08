class Empty(Exception):
    def __init__(self, msg):
        self.msg = msg  

    def __str__(self):
        return self.msg

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        
        self._front = (self._front - 1 + len(self._data)) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[((self._front + self._size) % len(self._data)) - 1]
        self._size = self._size - 1 + len(self._data) % len(self._data)
        return answer

a = input('Put a string which you want to check: ')
q = ArrayQueue()
for i in range(int(len(a)/2)):
    q.enqueue(a[i])
    q.add_first(a[-1-i])

for i in range(int(len(a)/2)):
    if q.pop() != q.dequeue():
        print(a + ' is not a palindrome')
        exit()
print(a + ' is a palindrome')
    
    