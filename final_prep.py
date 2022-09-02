#bubble sort

from ast import Pass


def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [4, 3, 2, 1, -10, 100, 20, 69, 8]
print("Actual_array",arr)
# print(bubble_sort(arr))

def bubble_sort_recursive(a, length):
    if length == 1:
        return a
    for i in range(length-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return bubble_sort_recursive(a, length-1)
    # return bubble_sort_recursive(a[:-1]) + [a[-1]]

# print(bubble_sort_recursive(arr, len(arr)))
# print(arr[:-1]+[arr[-1]])

#--------------------------------------------------------------
#selection_sort

def selection_sort_min(a):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def selection_sort_max(a):
    for i in range(len(a)-1, 0, -1):   
        max_idx = i
        for j in range(len(a)-2, 1, -1):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a
        # print(a[i])

# print(selection_sort_max(arr))

def selection_sort_recursive(a, min):
    if min == len(a)-1:
        return
    min_idx = min
    for j in range(min+1, len(a)):
        if a[j]<a[min_idx]:
            min_idx = j
    a[min], a[min_idx] = a[min_idx], a[min]
    selection_sort_recursive(a, min+1)

# selection_sort_recursive(arr, 0)
# print(arr)

#--------------------------------------------------------------
#insertion_sort

def insertion_sort(a):
    for i in range(len(a)):
        for j in range(i-1, -1, -1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# print(insertion_sort(arr))

def insertion_sort_recursive(a, i):
    if i == len(a):
        return
    for j in range(i-1, -1, -1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    insertion_sort_recursive(a, i+1)

# insertion_sort_recursive(arr, 0)
# print(arr)

#--------------------------------------------------------------
#linear_search

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# a = linear_search(arr, 6)
# if a!=-1:
#     print("Found at index",a)
# else:
#     print("Not found")

def linear_search_recursive(a, l, i, x):
    if i == l:
        return -1
    if a[i] == x:
        return i
    return linear_search_recursive(a, l, i+1, x)

# a = linear_search_recursive(arr, len(arr), 0, 8)
# if a!=-1:
#     print("Found at index",a)
# else:
#     print("Not found")


#--------------------------------------------------------------
#binary_search
def binary_search_recursive(a, l, r, x):  #this search is only for sorted array
    if l>=r:
        return -1
    else:
        m = (l+r)//2
        if a[m]==x:
            return m
        elif x<a[m]:
            return binary_search_recursive(a, l, m-1, x)
        else:
            return binary_search_recursive(a, m+1, r, x)


arr_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = binary_search_recursive(arr_b, 0, len(arr)-1, 2)
# if a!=-1:
#     print("Found at index",a)
# else:
#     print("Not found")

#--------------------------------------------------------------
"""                             Hashing (Simulation)
Draw the contents of the hash table given the following conditions:
    ● The size of the hash table is 10.
    ● Linear Probing is used to resolve collisions.
    ● The hash function H(k) should be calculated in the following way where k is the element
      to be hashed:

      R(k) = summation of the digits in k
      If R(k) < 8
      H(k)= (R(k) + 6) mod (10)
      else
      H(k)= (R(k) - 2) mod (10)

mod (10)What values will be in the hash table after the following sequence of insertions?

            s3x5, 1aa8, 8bg, 1aw3, 2131, ft249, 1gfg6, 2po7, 8fd61, 54sds6

[Note: Draw the values using a hash table and show your work for partial credit.]"""

arrayH = [0]*10
def H(k):
    def R(k):
        sumation = 0
        for i in k:
            if 47 < ord(i) < 58:
                sumation = sumation + int(i) #ord(i)
        return sumation
    if R(k)<8:
        index = (R(k) + 6) % 10
    else:
        index = (R(k) - 2) % 10

    while arrayH[index] != 0:
        index = (index + 1) % 10
    
    arrayH[index] = k
    # return arrayH

arrH = ["s3x5", "1aa8", "8bg", "1aw3", "2131", "ft249", "1gfg6", "2po7", "8fd61", "54sds6"]
for i in arrH:
    H(i)
# print(arrayH)

#--------------------------------------------------------------
#Queue

class CirArray:
    def __init__(self, a, st, size):
        self.a = a
        self.start = st
        self.size = size
    
    def enqueue(self, val):
        end = (self.start+self.size)%len(self.a)
        self.a[end]=val
        self.size=(self.size+1)%len(self.a)

    def dequeue(self):
        temp = self.a[self.start]
        self.a[self.start]=0
        self.start=(self.start+1)%len(self.a)
        return temp

    def peek(self):
        return self.a[self.start]
    
arr=[0]*10
# a1=CirArray(arr, 0, 0)
# a1.enqueue(1)
# a1.enqueue(2)
# a1.enqueue(3)
# a1.dequeue()
# print("value",a1.a)
# print("PEEK",a1.peek())
# print(a1.start)