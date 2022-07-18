#Name   : Md. Ragib Asif
#ID     : 21101083
#Section: 06

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

#----------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedStack:
    cap = 25
    head = None
    pointer = -1

    def push(self, value):
        if self.pointer < self.cap:
            n = Node(value)
            if self.head == None:
                self.head = n
                self.pointer += 1
            else:
                n.next = self.head
                self.head = n
                self.pointer += 1
        else:
            return f'Stack overflowed'

    def peek(self):
        if self.pointer<-1:
            return f'Stack underflowed'
        if self.head == None:
            return None
        else:
            return self.head.value

    def pop(self):
        if self.pointer<-1:
            return f'Stack underflowed'
        elif self.pointer>=self.cap:
            return f'Stack overflowed'
        temp = self.head
        next = self.head.next
        self.head = next
        self.pointer -= 1
        return temp.value

#--------------------------------------------------------
string1 = "1+2*(3/4)"
string2 = "1+2*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14"
string3 = "1+2*[3*3+{4-5(6(7/8/9)+10)}-11+(12*8)/{13+13}]+14"
string4 = "1+2]*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14"

#--------------------------------------------------------

def ArrayBraket(string):
    stack_obj = ArrayStack()
    pointer_obj = ArrayStack()
    counter = 1

    open = ['(', '[', '{']
    close = [')', ']', '}']

    for i in string:
        if stack_obj.peek() == None and i in close:
            return f"{string} \nThis expression is NOT correct. \nEror at character # {counter}. '{i}'- not opened."

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
        return f"{string} \nThis expression is NOT correct. \nEror at character # {pointer_obj.peek()}. '{stack_obj.peek()}'- not closed."

print(ArrayBraket(string1))

#--------------------------------------------------------

def LinkedBraket(string):
    stack_obj = LinkedStack()
    pointer_obj = LinkedStack()
    counter = 1

    open = ['(', '[', '{']
    close = [')', ']', '}']

    for x in string:
        if x in open:
            stack_obj.push(x)
            pointer_obj.push(counter)
        elif x in close:
            if stack_obj.peek() == None:
                return f"{string} \nThis expression is NOT correct. \nEror at character # {counter}. '{x}'- not opened."
            if stack_obj.peek()=='(' and x==')' or stack_obj.peek()=='[' and x==']' or stack_obj.peek()=='{' and x=='}':
                stack_obj.pop()
                pointer_obj.pop()
            else:
                break
    
        counter += 1
    if stack_obj.peek() == None: 
        return f'{string} \nThis expression is correct.'
    else: 
        return f"{string} \nThis expression is NOT correct. \nEror at character # {pointer_obj.peek()}. '{stack_obj.peek()}'- not closed."
print(LinkedBraket(string4))

