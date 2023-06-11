class MyQueue:
    def __init__(self):
        self.queue = []
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        if self.empty():
            self.stack1.append(x)
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1[i])
                self.stack1.pop(i)
            self.stack1.append(x)
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2[i])
                self.stack2.pop(i)

    def pop(self):
        self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def empty(self):
        if len(self.queue) <= 0:
            return True


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())    # Return 1
print(queue.pop())     # Return 1
print(queue.empty())   # Return False