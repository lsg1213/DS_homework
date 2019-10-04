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
            raise IndexError('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data.pop()

s = ArrayStack()
a = input('put a string which you want to decide palindrome or not\n')
if len(a) % 2 == 1:
    i = len(a) // 2 + 1
else:
    i = len(a) // 2
for j in range(i):
    s.push(a[j])


if len(s) > len(a) / 2:
    s.pop()
while not s.is_empty():
    if s.top() != a[i]:
        print(a, 'is not a palindrome string')
        exit()
    s.pop()
    i += 1

print(a, 'is a palindrome string')