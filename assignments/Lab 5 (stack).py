from tkinter import N


class ArrayStack:
    def __init__(self):
        self.cap = 25
        self.stack = [None]*self.cap
        self.pointer = -1

    def push(self, element):
        if self.pointer < self.cap:
            self.pointer += 1
            self.stack[self.pointer]= element
            
        else:
            return f'Stack overflowed'
        
    def pop(self):
        if self.pointer<-1:
            return f'Stack underflowed'
        elif self.pointer>=self.cap:
            return f'Stack overflowed'
        else:
            value = self.stack[self.pointer]
            self.stack[self.pointer] = None
            self.pointer -= 1
            return value
    
    def peek(self):
        if self.pointer<-1:
            return f'Stack underflowed'
        return self.stack[self.pointer]

    # def print(self):
    #     return self.stack

obj1 = ArrayStack()
obj1.push(6)
print(obj1.peek())
obj1.push(4)
# print(obj1.print())
print(obj1.pop())
print(obj1.peek())
# print(obj1.print())

#--------------------------------------------------------------------------------
print("GAP")
#--------------------------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    head = None

    def push(self, value):
        n = Node(value)
        if LinkedStack.head == None:
            LinkedStack.head = n
        else:
            n.next = LinkedStack.head
            LinkedStack.head = n

    def peek(self):
        return LinkedStack.head.value

    def pop(self):
        temp = LinkedStack.head
        next = LinkedStack.head.next
        LinkedStack.head = next
        return temp.value

obj2 = LinkedStack()
obj2.push(6)
print(obj2.peek())
obj2.push(4)
# print(obj2.print())
print(obj2.pop())
print(obj2.peek())
# print(obj2.print())