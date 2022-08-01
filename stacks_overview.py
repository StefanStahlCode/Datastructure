class Stack:
    def __init__(self):
        self.stack = []

#add method to add elements to stack, here always look at last element
    def add(self, ele):
        if ele not in self.stack:
            self.stack.append(ele)
            return True
        else:
            return False
    
#remove last element
    def remove(self):
        if len(self.stack) <= 0:
            return "No Element in Stack"
        else:
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())