# dynamic array

import ctypes
from time import time
def compute_average(n):
    data = DynamicArray()
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / float(n)

def compute_incre_average(n):
    data = DynamicArray()
    start = time()
    for k in range(n):
        data.append_incremental(None)
    end = time()
    return (end - start) / float(n)

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        self._c = 1000 #incremental constant

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def append_incremental(self, obj):  #resize the capacity with constant c
        if (self._n == self._capacity):
            self._resize(self._capacity + self._c)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self, c):
        return (c * ctypes.py_object)()


i = 100
print('1. doubling')
print('--------------------------------------------------------------------------')
while i <= 100000000:
    data = DynamicArray()
    print('data num: {}\t'.format(i) + 'time: {}'.format(compute_average(i)))
    i *= 10
print('--------------------------------------------------------------------------')
i = 100
print('2. incremental')
print('--------------------------------------------------------------------------')
while i <= 100000000:
    data = DynamicArray()
    print('data num: {}\t'.format(i) + 'time: {}'.format(compute_incre_average(i)))
    i *= 10
print('--------------------------------------------------------------------------')

