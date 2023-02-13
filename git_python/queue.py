from collections import deque

class queue():
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self,val=-1):
        return self.items.popleft()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__=='__main__':
    q=queue()
    print(q)

    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q)

    q.dequeue()
    print(q)
