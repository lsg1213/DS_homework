class Empty(Exception):
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

def test(string = ""):
    s = ArrayStack()
    if string == "":
        while True:
            try:
                a = input('put a string which you want to decide palindrome or not\n')
                if a == "":
                    continue
                break
            except:
                print('wrong input')
    else:
        a = str(string)
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
            if string == "":
                print(a, 'is not a palindrome string')
                exit()
            else:
                return True
        s.pop()
        i += 1
    if string == "":
        print(a, 'is a palindrome string')
    else:
        return True

if __name__ == "__main__":
    test()