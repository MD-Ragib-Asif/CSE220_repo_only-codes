


class ArrayStack:
    '''Array stack is a stack class that uses an array as its underlying storage'''
    def __init__(self) -> None:

        self.array = []
        self.pointer = -1

    def push(self,element:any) -> None:
        '''Pushes an element to the stack'''
        self.array += [element]
        self.pointer += 1
    
    def peek(self) -> any:
        '''returns the last value of the stack'''
        if len(self.array) < 1: return False
        return self.array[-1]

    def pop(self) -> any:
        '''Pops out the last element of the stack'''
        value = self.array[-1]
        
        self.array = [self.array[x] for x in range(self.pointer)]
        self.pointer -= 1 
        return value

# array_stack = ArrayStack()
# array_stack.push(1)
# array_stack.push(2)
# array_stack.push(3)
# print(array_stack.peek())
# array_stack.pop()
# print(array_stack.peek())


class Node:
    def __init__(self,value) -> None:
        '''Node class for the implementation of the linked list'''
        self.value = value
        self.ref = None

class LinkedListStack:
    head = None
    
    def push(self,value):
        n = Node(value)
        if self.head == None:
            self.head = n
        else:
            n.ref = self.head
            self.head = n 
    
    def peek(self):
        return self.head.value
    
    def pop(self):
        temp = self.head
        self.head = self.head.ref
        temp.ref = None
        temp.value = None 

# list_stack = LinkedListStack()

# list_stack.push('hello')
# list_stack.push('hi')
# print(list_stack.peek())
# list_stack.pop()
# print(list_stack.peek())



first = '1+2*(3/4)'
 
second = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
 
third = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'


def bracket (word:str) -> bool:
    '''Checks if the brackets in a string are balanced'''
    stack = ArrayStack()
    eror_stack = ArrayStack()
    # print(stack.peek())
    counter = 1
    
    for x in word:
        # if stack.peek() == False and x in [')','}',']']:
        #     return f'{word}\nThis expression is not correct\nEror at #{counter+1}. {x} was not started'
        if stack.peek() == False and x in [')','}',']']: return f'{word}\nThis expression is not correct\nEror at #{counter+1}. {x} was not started'
        if stack.peek() == False and x in ['(','{','[']:
            stack.push(x)
            eror_stack.push(counter)
        elif stack.peek() in ['(','[','{'] and x in ['(','{','[']:
            stack.push(x)
            eror_stack.push(counter)
        
        if stack.peek() =='(' and x == ')' or stack.peek() =='[' and x == ']' or stack.peek() =='{' and x == '}' :
            stack.pop()
            eror_stack.pop()
        counter += 1
        # print(stack.array)
    if stack.peek() == False: return f'{word}\nThis expression is correct.'
    else: return f'{word}\nThis expression is not correct\nEror at #{eror_stack.peek()}. {stack.peek()} was not closed'


print(bracket(third))