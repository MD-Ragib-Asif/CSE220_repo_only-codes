#Name   : Md. Ragib Asif
#ID     : 21101083
#Section: 06

class ArrayStack:
    pointer = -1
    def __init__(self):
        self.cap = 50
        self.stack = [None]*self.cap
        

    def push(self, element):
        if self.pointer < self.cap-1:
            self.pointer += 1
            self.stack[self.pointer]= element
        else:
            print('Stack overflowed')
        
    def pop(self):
        if self.pointer==-1:
            return f'Stack underflowed'
        else:
            value = self.stack[self.pointer]
            self.stack[self.pointer] = None
            self.pointer -= 1
            return value
    
    def peek(self):
        if self.pointer==-1:
            return f'Stack underflowed'
        return self.stack[self.pointer]

# obj1 = ArrayStack()
# obj1.push(5)
# obj1.push(4)
# obj1.push(3)
# obj1.push(2)
# obj1.push(1)
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# # print(obj1.peek())
# print(obj1.pop())


#----------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedStack:
    cap = 50
    head = None
    pointer = -1

    def push(self, value):
        if self.pointer < self.cap-1:
            self.pointer += 1
            n = Node(value)
            if self.head == None:
                self.head = n
            else:
                n.next = self.head
                self.head = n
                
        else:
            print('Stack overflowed')

    def peek(self):
        if self.pointer == -1:
            return f'Stack underflowed'
        if self.head == None:
            return None
        else:
            return self.head.value

    def pop(self):
        if self.pointer == -1:
            return f'Stack underflowed'
        
        temp = self.head
        next = self.head.next
        self.head = next
        self.pointer -= 1
        return temp.value

# obj1 = LinkedStack()
# obj1.push(5)
# obj1.push(4)
# obj1.push(3)
# obj1.push(2)
# obj1.push(1)
# # obj1.push(7)
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.pop())
# print(obj1.peek())
# print(obj1.pop())

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
        if stack_obj.peek() == 'Stack underflowed' and i in close:
            return f"{string} \nThis expression is NOT correct. \nEror at character # {counter}. '{i}'- not opened."

        if stack_obj.peek() == 'Stack underflowed' and i in open:
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
    if stack_obj.peek() == 'Stack underflowed': 
        return f'{string} \nThis expression is correct.'
    else: 
        return f"{string} \nThis expression is NOT correct. \nEror at character # {pointer_obj.peek()}. '{stack_obj.peek()}'- not closed."

print(ArrayBraket(string2))

#--------------------------------------------------------
print('**************************************')
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
            if stack_obj.peek() == 'Stack underflowed':
                return f"{string} \nThis expression is NOT correct. \nEror at character # {counter}. '{x}'- not opened."
            if stack_obj.peek()=='(' and x==')' or stack_obj.peek()=='[' and x==']' or stack_obj.peek()=='{' and x=='}':
                stack_obj.pop()
                pointer_obj.pop()
            else:
                break
    
        counter += 1
    if stack_obj.peek() == 'Stack underflowed': 
        return f'{string} \nThis expression is correct.'
    else: 
        return f"{string} \nThis expression is NOT correct. \nEror at character # {pointer_obj.peek()}. '{stack_obj.peek()}'- not closed."
print(LinkedBraket(string3))

