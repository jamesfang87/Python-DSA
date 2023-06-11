class MinStack:
    def __init__(self, size=10):
        self.size = size
        self.data = []

    def push(self, x):
        if len(self.data) >= self.size:
            print('Stack overflow')
        else:
            self.data.append(x)

    def pop(self):
        if len(self.data) <= 0:
            print('Stack underflow')
        else:
            self.data.pop()

    def top(self):
        if len(self.data) <= 0:
            print('Stack underflow')
        else:
            return self.data[-1]

    def getMin(self):
        if len(self.data) <= 0:
            print('Stack underflow')
        else:
            return min(self.data)

    def getMax(self):
        if len(self.data) <= 0:
            print('Stack underflow')
        else:
            return max(self.data)


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # return -3
print(minStack.pop())      # return (-3, -3)
print(minStack.top())      # return 0
print(minStack.getMin())   # return -2