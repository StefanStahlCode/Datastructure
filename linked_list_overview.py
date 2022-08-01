#a linked list is a sequence of data elements, connected via links, in a normal or single linked list only the next element is linked
#python uses linked lists via self impemented nodes

class Node:
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.next = None #used to point to the next value

class linkedL:
    def __init__(self):
        self.headvalue = None #pointer to start of linkedlist
    
    def listprint(self):#print the list
        printvalue = self.headvalue
        while printvalue:
            print(printvalue.datavalue)
            printvalue = printvalue.next

    def insertBeginning(self, ele):
        NewNode = Node(ele)
        NewNode.next = self.headvalue
        self.headvalue = NewNode

    def insertEnd(self, ele):
        NewNode = Node(ele)
        if self.headvalue is None:
            self.headvalue = NewNode
            return

        
        lastel = self.headvalue
        while lastel.next:
            lastel = lastel.next
        lastel.next = NewNode  

#function to insert new element after given element
    def insertEle(self, ele, pos_node):
        NewNode = Node(ele)
        if pos_node is None:
            print("position is None")
            return
        
        NewNode.next = pos_node.next
        pos_node.next = NewNode

#function to insert element at given position, starting with 0 as the head
    def insertPos(self, ele, pos):
        NewNode = Node(ele)
        if pos == 0:
            self.insertBeginning(NewNode)
            return
        elif pos < 0:
            print("Error: List starts at 0")
            return
        current = self.headvalue
        while (pos - 1) > 0:
            current = current.next
            pos = pos -1
        NewNode.next = current.next
        current.next = NewNode

#remove specific item
    def removeEle(self, Removekey):
        Headvalue = self.headvalue

        if Headvalue is not None:
            if Headvalue.datavalue == Removekey:
                self.headvalue = Headvalue.next
                Headvalue = None
                return
        
        while Headvalue is not None:
            if Headvalue.datavalue == Removekey:
                break
            prev = Headvalue
            Headvalue = Headvalue.next
        
        if Headvalue is None:
            print("Element not in List")
            return
        
        prev.next = Headvalue.next
        Headvalue = None







list1 = linkedL()
list1.headvalue = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

#link first node to second
list1.headvalue.next = e2

#second to third
e2.next = e3

list1.insertBeginning("Sun")
list1.insertEnd("Thur")
list1.insertEle("Fri", list1.headvalue.next.next.next.next)
list1.insertPos("Sat", 6)
list1.listprint()
list1.removeEle("Wed")
list1.listprint()

