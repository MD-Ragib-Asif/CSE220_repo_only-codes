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
# obj1.push(6)
# # print(obj1.peek())
# obj1.push(4)
# # print(obj1.print())
# print(obj1.pop())
# print(obj1.peek())
# print(obj1.print())

# string = "1+2*(3/4)"
# string = "1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
# string = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
string = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"

size = len(string)
opened = ['[', '{', '(']
closed = [']', '}', ')']
leave=0
for i in range(len(string)):
    if leave!=0:
        break
    if string[i] in opened:
        obj1.push(string[i])
    elif string[i] in closed:
        check = obj1.peek()
        for j in range(len(closed)):
            if string[i] == closed[j]:
                if check == opened[j]:
                    obj1.pop()
                else:
                    print(f'This expression is NOT correct. \nError at character # {i+1}. ‘{string[i]}‘- not opened.')
                    leave+=1
                    break

if leave==0:

    if obj1.peek()!=None:
        for k in range(len(string)):
            if string[k]==obj1.peek():
                idx=k
        print(f'This expression is NOT correct. \nError at character # {idx+1}. ‘{obj1.peek()}‘- not closed.')
    else:
        print("This expression is correct.")