#1. Shift Left k Cells
def shiftLeft(source, k):
  for j in range(k):
    i = 0
    while(i<len(source)-1):
      source[i] = source[i+1]
      i+=1
    source[len(source)-1] = 0

source=[10,20,30,40,50,60]
shiftLeft(source,3)
print("task 1: ",source)


#2. Rotate Left k cells
def rotateLeft(source, k):
  for j in range(k):
    i = 0
    while(i<len(source)-1):
      source[i], source[i+1] = source[i+1], source[i]
      i+=1

source=[10,20,30,40,50,60]
rotateLeft(source,3)
print("task 2: ",source)


#3. Shift Right k Cells
def shiftRight(source, k):
  for j in range(k):
    i = len(source)-1
    while(i>0):
      source[i] = source[i-1]
      i-=1
    source[0] = 0

source=[10,20,30,40,50,60]
shiftRight(source,3)
print("Task 3: ",source)


#4. Rotate Right k cells
def rotateRight(source, k):
  for j in range(k):
    i = len(source)-1
    while(i>0):
      source[i], source[i-1] = source[i-1], source[i]
      i-=1

source=[10,20,30,40,50,60]
rotateRight(source,3)
print("Task 4: ",source)


#5. Remove an element from an array
def remove(source, size, idx):
  i = idx
  while(i<len(source)-1):
    source[i] = source[i+1]
    i+=1
  source[len(source)-1]=0

source=[10,20,30,40,50,0,0]
remove(source,5,2)
print("Task 5: ",source)


#6. Remove all occurrences of a particular element from an array
def removeAll( source, size, element):

  for k in range(size):
    i=0
    for j in source:
      if j == element:
        remove(source, size, i)
        break
      i+=1
    
source=[10,30,2,2,50,2,2,0,0]
removeAll(source,7,2)
print("Task 6: ",source)


#7. Splitting an Array
def split(source):
  count=0
  for i in range(1, len(source)-1):
    left=0
    right=0
    for j in range(0,i):
      left+=source[j]
    for k in range(i,len(source)):
      right+=source[k]
    if left==right:
      count+=1

  if count>0:
    return True
  else:
    return False

source1 =  [1, 1, 1, 2, 1] #true
source2 =  [2, 1, 1, 2, 1] #false
source3 =  [10, 3, 1, 2, 10] #true
print("Task 7: ")
print(split(source1))
print(split(source2))
print(split(source3))


def array_series(n):
  x= [x for x in range(n,0,-1)]
  y=[]
  z=""

  for j in range(n):
    q = [m for m in x]
    q[j]=0
    y= x+y 
    x=q
  # print("Array: ",y)
  
  i =0        # this loop is to only match the output same as question
  for m in range(n):
    for l in range(n):
      if m==n-1 and l==n-1:
        z=z+str(y[i])
      else:
        z=z+str(y[i])+","
      i+=1
    z+=" "
  z="{ "+z+"}"

  return z

  
n=int(input("Please enter number for task 8: "))
print(array_series(n))


#9. Max Bunch Count
def bunch_count(source):
  element = source[0]
  count=0
  max=0
  for i in source:
    if element == i:
      count+=1
    else:
      count =1
    element = i
    if count>max:
      max = count

  return max

print("Task 9.1: ",bunch_count([1, 2, 2, 3, 4, 4, 4]))
print("Task 9.2: ",bunch_count([1,1,2, 2, 1, 1,1,1]))


#10. Repetition
def repetition(source):
  array=[]
  for j in source:
    if j not in array:
      array += [j]
  # print(array)
  
  empty_arr = [0]*len(array)
  for i in source:
    for k in range(len(array)):
      if i==array[k]:
        empty_arr[k]+=1
  # print(empty_arr)

  count = 0
  for l in range(len(empty_arr)):
    for m in range(l+1, len(empty_arr)):
      if empty_arr[l]==empty_arr[m] and empty_arr[l]>1:
        count += 1

  if count > 0:
    return True
  else:
    return False


print("Task 10.1: ",repetition([4,5,6,6,4,3,6,4]))
print("Task 10.2: ",repetition([3,4,6,3,4,7,4,6,8,6,6]))