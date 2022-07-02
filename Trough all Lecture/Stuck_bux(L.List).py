class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None

class Stack:
    head=None
    def push(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            n=Node(data)
            n.ref=self.head
            self.head=n
    def peek(self):
        return(self.head.value)

    def pop(self):
        temp=self.head
        self.head-self.ref
        temp.value = None
        temp.ref = None

stack = Stack()
stack.push(1)
print(stack.peek())

stack.push(2)
print(stack.peek())
