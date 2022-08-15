# Name    : Md. Ragib Asif
# ID      : 21101083
# Section : 06
#--------------------------------------------------------------

print("--------------------Task 1---------------------")
#a
def factorial(num):

    if num == 0:
        return 1
    
    num = num * factorial(num-1)
    return num

print(factorial(5))

#b
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci (num -1) + fibonacci(num -2)

print(fibonacci(7))

#c
def array(arr, idx):
    if idx >= len(arr):
        return
    print(arr[idx])
    array(arr, idx+1) 
    
    

array1 = [1,2,3,4,5]
array(array1, 0)

#d
import math
def powerN(a, b):
    if b==0:
        return 1
    return a*powerN(a, b-1)
    
print(powerN(3,2))

print("--------------------Task 2---------------------")
#a
def converts(n):
    if n/2 == 0:
        return
    
    converts(n//2)
    print(n%2)

converts(97)

#b
class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:
    
    def __init__(self, a):
        self.head = None
        tail = None

        if type(a)==list:
            for i in a:
                n = Node(i, None)
                if self.head == None:
                    self.head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n
        elif type(a)==LinkedList:
            newHead = a.head
            while newHead is not None:
                newNode = Node(newHead.element, None)
                if self.head == None:
                    self.head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                newHead = newHead.next
        else:
            self.head = a


def sum(n):
    if n == None:
        return 0
    return n.element + sum(n.next)

a1 = [10, 20, 30, 40]
obj1= LinkedList(a1)
print(sum(obj1.head))

#c
def printLinkedB(n):
  if n == None:
    return
  printLinkedB(n.next)
  print(n.element)
  
printLinkedB(obj1.head)

print("--------------------Task 3---------------------")
def hocBuilder(height):
    if height == 1:
        return 8
    return 5 + hocBuilder(height-1)
print(hocBuilder(3))

print("--------------------Task 4---------------------")
#a
def pattern(num):
    
    if num==0:
        return
    pattern(num-1)
    for i in range(1, num+1): print(i, end="")
    print()
    

pattern(5)

#b
def pattern(num, n=1):
    
    if num==n-1:
        return
   
    a = ""
    for x in range(1, n+1): a+=str(x) 
    print(" "*(num-n) + a)
    pattern(num , n+1)

pattern(5)

print("--------------------Task 5---------------------")
class FinalQ: 
    def print(self,array,idx):
        if(idx<len(array)): 
            profit = self.calcProfit(array[idx]) #TO DO
            print("{}. Investment: {}; Profit: {}".format(idx+1, array[idx], profit))
            self.print(array, idx + 1)
        else:
            return
    
    def calcProfit(self,investment):
        #TO DO
        if investment % 100 != 0:
            return 0.0
        if investment < 25001:
            return 0.0
        if investment <=100000:
            return 45 + float(self.calcProfit(investment - 1000))
        elif investment > 100000:
            return 80 + float(self.calcProfit(investment - 1000))
  
#Tester 
array=[25000,100000,250000,350000] 
f = FinalQ() 
f.print(array,0)