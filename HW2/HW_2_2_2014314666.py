from math import floor, log2
import numpy as np
import time as time


class minHeap():
    def __init__(self):
        self._data = []
        self._data.append(None)
    
    def getDepth(self, index):
        return floor(log2(index))

    def insert(self, data):
        self._data.append(data)
        index = len(self._data) - 1
        
        self.upheap(index)

    def __len__(self):
        return len(self._data)

    def remove_min(self):
        res = self._data[1]
        if len(self._data) > 2:
            self._data[1] = self._data.pop()
            self.downheap(1)
        else:
            self._data.pop()
        return res

    def printHeap(self):
        for i in self._data:
            if i == None:
                continue
            print(i, end=' ')

    def downheap(self, index):
        while True:
            right = index * 2 + 1
            left = index * 2
            if right <= len(self._data) - 1:
                if self._data[right] > self._data[left]:
                    self._data[index], self._data[left] = self._data[left], self._data[index]
                    index = left
                elif self._data[right] < self._data[left]:
                    self._data[index], self._data[right] = self._data[right], self._data[index]
                    index = right
                else:
                    return
            elif left == len(self._data) - 1:
                if self._data[left] < self._data[index]:
                    self._data[index], self._data[left] = self._data[left], self._data[index]
                return
            else:
                return
        

    def upheap(self, index):
        while index != 1:
            if self._data[index] < self._data[index // 2]:
                self._data[index], self._data[index // 2] = self._data[index // 2], self._data[index]
                index = index // 2
            else:
                break
        

if __name__ == "__main__":
    datasheet = np.arange(100000000)
    b = np.random.choice(datasheet, size=10).flatten()
    print('raw list:', b)
    c = minHeap()
    for i in b:
        c.insert(i)
    print('show heap:\n[', end='')
    c.printHeap()
    print(']')
    print('sorted list:\n[', end='')
    while len(c) >= 2:
        print(c.remove_min(), end=' ')
    print(']')
    n = 1
    while n <= 1000:
        a = np.random.choice(np.arange(100000),size=1000*n)
        h = minHeap()
        insertTime = np.array([], dtype='float64')
        removeTime = np.array([], dtype='float64')
        for i in a:
            s_time = time.time()
            h.insert(i)
            insertTime = np.append(insertTime, time.time() - s_time)
        for i in a:
            s_time = time.time()
            h.remove_min()
            removeTime = np.append(removeTime, time.time() - s_time)

        print('{} size'.format(1000 * n))
        print('inserting time: {}\nremove time: {}'.format(np.mean(insertTime), np.mean(removeTime)))
        n *= 10
    