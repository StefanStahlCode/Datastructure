#A Queue Adds Elements at the end, new elements gets added at the end
#Deque: A Queue where you can add and remove elements from both sides
#Priority Queue: Adds a Priority Element, the elements with the highest priority get removed first

#stacks allow easy access to the top most object, as you only add or remove the elements at the first position



class Queue:
    def __init__(self, head=None):
        self.storage = [head]
        self.next = None

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] 

    def dequeue(self):
        return_element = self.storage[0]
        self.storage.pop(0)
        return return_element
    

q = Queue(1)
q.enqueue(2)
q.enqueue(3)

print (q.peek())

print (q.dequeue())

q.enqueue(4)

print (q.dequeue())

print (q.dequeue())

print (q.dequeue())
q.enqueue(5)

print (q.peek())