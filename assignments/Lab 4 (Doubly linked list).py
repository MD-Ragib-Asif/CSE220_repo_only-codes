class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p


class DoublyList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array.
    self.head = Node(None, None, None)
    self.head.prev = self.head.next = self.head
    t=self.head

    for i in a:
      newNode = Node(i, self.head, t)
      t.next = newNode
      t = newNode
    self.head.prev = t


  
  # Counts the number of Nodes in the list
  def countNode(self):
    count = 0
    n=self.head.next

    while n != self.head:
      count+=1
      n=n.next

    return count
  
  # prints the elements in the list
  def forwardprint(self):
    n = self.head.next
    for i in range(self.countNode()):
      if i != self.countNode()-1:
        print(n.element, end=",")
      else:
        print(n.element)
      n=n.next

  # prints the elements in the list backward
  def backwardprint(self):
    n = self.head.prev
    for i in range(self.countNode()):
      if i != self.countNode()-1:
        print(n.element, end=",")
      else:
        print(n.element)
      n=n.prev

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    n = self.head.next
    if idx<0 or idx>=self.countNode():
      if idx<0:
        print(f'Index can not be negative')
      elif idx>=self.countNode():
        print(f'Unfortunate index out of bound')
      return None

    else:
      for i in range(self.countNode()):
        if i == idx:
          return n
        n = n.next
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    n = self.head.next
    for i in range(self.countNode()):
      if n.element==elem:
        return i
      n = n.next
    return -1

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    n=self.head.next
    newNode = Node(elem, None, None)

    if(idx<0 or idx>self.countNode()):
      raise Exception("Invalid index")

    if idx ==0:
      pointer = self.head
      newNode.prev = pointer
      newNode.next = pointer.next
      pointer.next = newNode 
      pointer.next.next.prev = newNode
      return
      
    else:
      pointer = self.nodeAt(idx-1)
      newNode.prev = pointer
      newNode.next = pointer.next
      pointer.next = newNode 
      pointer.next.next.prev = newNode

    n = n.next
    return self.head

  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    n=self.head.next
    if(idx<0 or idx>=self.countNode()):
      raise Exception("Invalid index")

    
    for i in range(self.countNode()):
      
      if i == idx:
        removed = self.nodeAt(idx)
        prev = removed.prev
        next = removed.next
        prev.next = next
        next.prev = prev

      n = n.next
    return str(removed.element)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,85.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.