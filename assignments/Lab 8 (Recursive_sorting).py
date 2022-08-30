#Name    : Md. Ragib Asif
#ID      : 21101083
#Section : 06

#1. Sort an array RECURSIVELY using selection sort algorithm.
def rec_sel_sorting(A, i):
    if i == len(A)-1:
        return
    # min = A[i]
    min_idx = i
    for j in range(i, len(A)):
        if A[j] < A[min_idx]:
            min_idx = j
            # min = A[j]

    A[min_idx], A[i] = A[i], A[min_idx]
    rec_sel_sorting(A, i+1)

a2 = [3, 5, 8, 4, 1, 9, -2]
rec_sel_sorting(a2, 0)
print(a2)


#2. Sort an array RECURSIVELY using insertion sort algorithm.
def rec_ins_sort(A, i):
    if i == len(A):
        return
    for j in range(i-1, -1, -1):
        if A[j]>A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]


    rec_ins_sort(A, i+1)

a2 = [3, 5, 8, 4, 1, 9, -2]
rec_ins_sort(a2, 1)
print(a2)


#3. Sort a singly linked sequential list using bubble sort algorithm.
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

    def countNode(self):
        count = 0
        n=self.head
        while n is not None:
            count+=1
            n=n.next
        return count

    def printList(self):
        n = self.head
        for i in range(self.countNode()):
            if n.next is not None:
                print(n.element, end=",")
            else:
                print(n.element,end=".")
            n=n.next
        print()

def bubble_sort(ll,head=''):
    if head == '':
        head = ll.head

    if head.next == None:
        return
    def swap(head):
        if head.next == None:
            return
        if head.element > head.next.element:
            head.element, head.next.element = head.next.element, head.element
        swap(head.next)
    swap(ll.head)
    bubble_sort(ll,head.next)



ll = LinkedList([78, 20, 10, 32, 1, 5])
bubble_sort(ll)
ll.printList()

#4. Sort a singly linked sequential list using selection sort algorithm.
def selection_sort(head):
    i = head
    while (i.next != None) :
        cur = i.element
        visiting = i
        j = i.next
        while (j != None) :
            if (j.element < visiting.element) :
                visiting = j
            j = j.next
        if (visiting.element < cur) :
            temp = i.element
            i.element = visiting.element
            visiting.element = temp
        i = i.next


ll2 = LinkedList([78, 20, 10, 32, 1, 5])
selection_sort(ll2.head)
ll2.printList()


#5. Sort a DOUBLY linked sequential list using insertion sort algorithm.
class Node:
    def __init__(self, element, next=None, prev= None ): 
        self.element = element
        self.next = next 
        self.prev = prev
    

class DoublyList:
    def __init__(self,nodes):
        self.head = None 
        tail = None 
        prev = None 
        if len(nodes) < 1:
            print('Array can not be empty')
        else:
            for x in nodes:
                n = Node(x)
                if self.head == None:
                    self.head = n
                    tail = n 
                    prev = n 
                    self.length = 1
                else:
                    tail.next = n 
                    n.prev = prev
                    tail = n
                    prev = n
                    self.length += 1 


    def showList(self):
        if self.head == None: 
            print('Empty list')
        else:
            pointer = self.head
            y = self.length
            for x in range(y):
                if x == y-1: 
                    print(pointer.element)
                else: 
                    print(pointer.element,end ='<->')
                pointer = pointer.next

def doulby_ll_insertion_sort(pointer):
    if pointer == None:
        return
 
    def dl_insertion(prevNode,pointer):
        if prevNode == None or pointer == None:
            return 

        if pointer.element < prevNode.element:
            pointer.element , prevNode.element = prevNode.element , pointer.element

        dl_insertion(prevNode.prev,pointer.prev)
    dl_insertion(pointer,pointer.next)
    doulby_ll_insertion_sort(pointer.next)


dl1 = [100,5,6,7,1]
dl2 = DoublyList(dl1)
doulby_ll_insertion_sort(dl2.head)
dl2.showList()



#6. Implement binary search algorithm RECURSIVELY.
def b_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return b_search(arr, low, mid - 1, x)
		else:
			return b_search(arr, mid + 1, high, x)

	else:
		return -1

arr = sorted([10,-3,7,8,1,5,2])
x = 10
result = b_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Present at {} index".format(result))
else:
	print("Not present")



#7. Implement a recursive algorithm to find the n-th Fibonacci number using memoization.
arr = []
def runner(n):
    global arr
    arr=[None]*(n+1)
    arr[0] = 0
    arr[1] = 1
    return memoization(n)
def memoization(n):
    global arr
    if arr[n]!= None:
        return arr[n]
    else:
        arr[n] = memoization(n-1)+memoization(n-2)
        return arr[n]

print(runner(40))