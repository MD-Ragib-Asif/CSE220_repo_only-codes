class Stack:
    stack=[]
    pointer=-1
    def push(self,element):
        Stack.stack.append(element)
        Stack.pointer+=1
    def peek(self):
        return(Stack.stack[Stack.pointer])
        self.value=Stack.stack[Stack.pointer]
    def pop(self):
        Stack.stack=Stack.stack[:-1]
        Stack.pointer-=1
        return self.value
stack1=Stack()
stack1.push(2)
print(stack1.peek())
stack1.push(5)
print(stack1.peek())