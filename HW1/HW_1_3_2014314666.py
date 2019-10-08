from time import time
from random import random
from HW_1_2_2014314666 import ArrayStack, test

def checking(): #모든 case는 palindrome 하다
    test_case = []
    i = 10
    while i <= 500:
        a = ""
        for j in range(i):
            a += str(int(random() * 10 ** 5))
        a = a + a[::-1]
        test_case.append(a)
        i += 10

    for i in test_case:
        q = ArrayQueue()
        dq_st = time()
        dq_res = False
        for j in range(int(len(i)/2)):
            q.enqueue(i[j])
            q.add_first(i[-1-j])

        for j in range(int(len(i)/2)):
            if q.pop() != q.dequeue():
                dq_res = False
                break
            elif j == int(len(i)/2) - 1:
                dq_res = True
        dq_end = time()

        s_st = time()
        s_res = test(i)
        s_end = time()
        if not (dq_res and s_res):
            print('잘못된 input')
            exit()
        print('{}글자 테스트\ndq: {}\nstack: {}\n'.format(len(i), dq_end - dq_st, s_end - s_st))
        

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



if __name__ == "__main__":
    menu = 0
    while True:
        try:
            menu = int(input('1. 디큐로 팰린드롬 검사하기\n2. 스택과 디큐로 테스팅하기(모든 경우는 팰린드롬)\n'))
            if (menu == 1 or menu == 2):
                break
        except:
            print('wrong input')
    if menu == 1:
        a = input('Put a string which you want to check: ')
        q = ArrayQueue()
        for i in range(int(len(a)/2)):
            q.enqueue(a[i])
            q.add_first(a[-1-i])

        for i in range(int(len(a)/2)):
            if q.pop() != q.dequeue():
                print(a + ' is not a palindrome')
                exit()
            elif i == int(len(a)/2) - 1:
                print(a + ' is a palindrome')
    elif menu == 2:
        checking()