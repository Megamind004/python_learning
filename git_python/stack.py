class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,val):
        self.items.append(val)

    def pop(self,val=-1): 
        return self.items.pop(val)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__=='__main__':
    s = stack()
    print(s)

    print(s.is_empty())
    s.push(3)
    s.push(40)
    s.push(4)
    s.push(5)
    s.push(6)

    print(s)
    s.pop(3)
    print(s)
    s.pop()
    print(s)
