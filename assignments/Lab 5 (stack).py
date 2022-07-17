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
        if LinkedStack.head == None:
            return None
        else:
            return LinkedStack.head.value

    def pop(self):
        temp = LinkedStack.head
        next = LinkedStack.head.next
        LinkedStack.head = next
        return temp.value

obj2 = LinkedStack()
# obj2.peek()
obj2.push(6)
print(obj2.peek())
obj2.push(4)
# print(obj2.print())
print(obj2.pop())
print(obj2.peek())
print(obj2.pop())
# print('error'.format(obj2.peek()))
# print(obj2.print())

#--------------------------------------------------------
string1 = "1+2*(3/4)"
string2 = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
string3 = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
string4 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

#--------------------------------------------------------

def ArrayBraket(string):
    stack_obj = ArrayStack()
    pointer_obj = ArrayStack()
    counter = 0

    open = ['(', '[', '{']
    close = [')', ']', '}']

    for i in string:
        if stack_obj.peek() == None and i in close:
            return f"{string} \nThis expression is NOT correct. \nEror at #{counter+1}. '{i}'- not opened."

        if stack_obj.peek() == None and i in open:
            stack_obj.push(i)
            pointer_obj.push(counter)

        elif stack_obj.peek() in open and i in open:
            stack_obj.push(i)
            pointer_obj.push(counter)
        
        if stack_obj.peek() =='(' and i == ')' or stack_obj.peek() =='[' and i == ']' or stack_obj.peek() =='{' and i == '}':
            stack_obj.pop()
            pointer_obj.pop()
        counter += 1
        # print(stack.array)
    if stack_obj.peek() == None: 
        return f'{string} \nThis expression is correct.'
    else: 
        return f'{string} \nThis expression is not correct \nEror at #{pointer_obj.peek()+1}. {stack_obj.peek()} was not closed'

print(ArrayBraket(string2))

#--------------------------------------------------------

def LinkedBraket(string):
    stack_obj = LinkedStack()
    pointer_obj = LinkedStack()
    counter = 0

    open = ['(', '[', '{']
    close = [')', ']', '}']

    for i in string:
        if stack_obj.peek() == LinkedStack and i in close:
            return f"{string} \nThis expression is NOT correct. \nEror at #{counter+1}. '{i}'- not opened."

        if stack_obj.peek() == LinkedStack and i in open:
            stack_obj.push(i)
            pointer_obj.push(counter)

        elif stack_obj.peek() in open and i in open:
            stack_obj.push(i)
            pointer_obj.push(counter)
        
        if stack_obj.peek() =='(' and i == ')' or stack_obj.peek() =='[' and i == ']' or stack_obj.peek() =='{' and i == '}':
            stack_obj.pop()
            pointer_obj.pop()
        counter += 1
        # print(stack.array)
    if stack_obj.peek() == LinkedStack: 
        return f'{string} \nThis expression is correct.'
    else: 
        return f'{string} \nThis expression is not correct \nEror at #{pointer_obj.peek()+1}. {stack_obj.peek()} was not closed'

print(LinkedBraket(string4))
