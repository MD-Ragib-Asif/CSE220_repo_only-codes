#Task 1
from queue import Queue

def reverse_queue(queue):
	# Base case
	if queue.empty():
		return

	# Dequeue current item (from front)
	item = queue.queue[0]
	queue.get()

	# Reverse remaining queue
	reverse_queue(queue)

	# Enqueue current item (to rear)
	queue.put(item)


def print_queue(queue):
	while not queue.empty():
		print(queue.queue[0], end=" ")
		queue.get()
	print()


# Driver Code
q = Queue()
q.put(1)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(8)
reverse_queue(q)
print_queue(q)


print("********************************************************")


#task 2
from queue import Queue

def interLeaveQueue(q):

	# To check the even number of elements
	if (q.qsize() % 2 != 0):
		print("Input even number of integers.")

	# Initialize an empty stack of int type
	s = []
	halfSize = int(q.qsize() / 2)

	# put first half elements into
	# the stack queue:5 6 7 8,
	# stack: 4(T) 3 2 1
	for i in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# enqueue back the stack elements
	# queue: 5 6 7 8 4 3 2 1
	while len(s) != 0:
		q.put(s[-1])
		s.pop()

	# dequeue the first half elements of
	# queue and enqueue them back
	# queue: 4 3 2 1 5 6 7 8
	for i in range(halfSize):
		q.put(q.queue[0])
		q.get()

	# Again put the first half elements into
	# the stack queue: 5 6 7 8,
	# stack: 1(T) 2 3 4
	for i in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# interleave the elements of queue and stack
	# queue: 1 5 2 6 3 7 4 8
	while len(s) != 0:
		q.put(s[-1])
		s.pop()
		q.put(q.queue[0])
		q.get()


# Driver Code

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(7)
q.put(8)
interLeaveQueue(q)
length = q.qsize()
for i in range(length):
	print(q.queue[0], end=" ")
	q.get()

print()
print("********************************************************")


#task 3
def isSubSequence(string1, string2, m, n):
	# Base Cases
	if m == 0:
		return True
	if n == 0:
		return False

	# If last characters of two
	# strings are matching
	if string1[m-1] == string2[n-1]:
		return isSubSequence(string1, string2, m-1, n-1)

	# If last characters are not matching
	return isSubSequence(string1, string2, m, n-1)


# Driver program to test the above function
# string1 = "hac"
# string2 = "cathartic"
# string1 = "bat"
# string2 = "table"
string1 = "abe"
string2 = "table"
if isSubSequence(string1, string2, len(string1), len(string2)):
	print ("Yes")
else:
	print ("No")


print("********************************************************")


#Task 4
def gcd(n1, n2):
    if (n2 != 0):
        return gcd(n2, n1 % n2)
    else:
        return n1

print(gcd(366, 6))


print("********************************************************")


#Task 5
def pairStar(Input, Output, i = 0) :
	
	# Append current character
	Output = Output + Input[i]

	# If we reached last character
	if (i == len(Input) - 1) :
		print(Output)
		return

	# If next character is same,
	# append '@'
	if (Input[i] == Input[i + 1]) :
		Output = Output + '@'

	pairStar(Input, Output, i + 1)

Input = "bbbb"
Output = ""
pairStar(Input, Output)