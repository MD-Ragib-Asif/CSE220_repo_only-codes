class CircularArray:
  def __init__(self, lin, st, sz):
    # Initializing Variables
    self.start = st
    self.size = sz
    self.cir = []
    #someting
    self.cir=[None]*len(lin)
    index = self.start
    i=0
    while i<self.size:
      self.cir[index] = lin[i]
      index = (index + 1) % len(self.cir)
      i+=1

    # print(self.cir)

    
    # if lin = [10, 20, 30, 40, None]
    # then, CircularArray(lin, 2, 4) will generate
    # cir = [40, null, 10, 20, 30]
    
    # To Do. 
    # Hints: set the values for initialized variables
  
  # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
    for i in range(len(self.cir)-1):
      print(self.cir[i], end=", ")
    print(self.cir[len(self.cir)-1])


  # Print from start index and total size elements
  def printForward(self): #Easy
    index = self.start
    i=0
    while i<self.size - 1:
      print(self.cir[index], end=", ")
      index = (index +1)%len(self.cir)
      i+=1
    print(self.cir[(self.start + self.size - 1) % len(self.cir)])

  
  def printBackward(self): #Easy
    index = (self.start + self.size - 1) % len(self.cir)
    i=0
    while i<self.size - 1:
      print(self.cir[index], end=", ")
      index = (index -1)%len(self.cir)
      i+=1
    print(self.cir[self.start])

  # With no null cells
  def linearize(self): #Medium
    lin_array = [None] * self.size
    index = self.start
    for i in range(len(lin_array)):
      lin_array[i]=self.cir[index]
      index = (index + 1) % len(self.cir)

    self.cir = lin_array

  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity): #Medium
    resize_array = [None] * newcapacity
    index = self.start
    index2 = self.start

    for i in range(self.size):
      resize_array[index2]=self.cir[index]
      index = (index + 1) % len(self.cir)
      index2 = (index2 + 1) % len(resize_array)

    self.cir = resize_array

  # This method will check whether the array is palindrome or not
  def palindromeCheck(self): #Hard
    i=0
    count=0
    while i<self.size:
      if self.cir[(self.start+i)%len(self.cir)] != self.cir[(self.start+self.size-1-i)%len(self.cir)]:
         count+=1
      i+=1
    if count!=0:
      print(f'This array is NOT a palindrome')
    else:
      print(f'This array is a palindrome')

  # This method will sort the values by keeping the start unchanged
  def sort(self):
    index = self.start
    for i in range(self.size):
      index2 = self.start
      for j in range(self.size):
        if self.cir[index] < self.cir[index2]:
          self.cir[index], self.cir[index2] = self.cir[index2], self.cir[index]
        index2 = (index2 + 1)%len(self.cir)
      index = (index + 1)%len(self.cir)
    # print(self.cir)

  # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
  def equivalent(self, cir_arr):
    index = self.start
    index2 = cir_arr.start

    for i in range(self.size):
      if self.cir[index] != cir_arr.cir[index2]:
        return False
      index2 = (index2 + 1)%len(cir_arr.cir)
      index = (index + 1)%len(self.cir)
    return True

  # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
  def intersection(self, c2):
    index = self.start
    lin_array=[]

    for i in range(self.size):
      if self.cir[index] in c2.cir:
        lin_array += [self.cir[index]]
      index = (index + 1)%len(self.cir)
    return lin_array

#==========================================================================================

# Tester class. Run this cell after completing methods in the upper cell and
# check the output

lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10

print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40

print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None

print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome

print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True

print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True

print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False

print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]