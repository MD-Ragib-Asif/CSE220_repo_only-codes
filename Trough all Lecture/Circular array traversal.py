#forward printing a circular array



def printForward(c,start,size):

    index=start

    i=0

    while(i<size):

        print(c[index])

        index=(index+1)%len(c)

        i=i+1


def printBackward(c,start,size):

    index=(start + size - 1) % len(c)

    i=0

    while(i<size):

        print(c[index])

        index=(index-1)%len(c)

        i=i+1

def backwardIteration(cir, start, size):
    k = (start + size - 1) % len(cir)
    for i in range(size):
        print(cir[k])
        k = k - 1
        if k == -1:
            k = len(cir) - 1


circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5

print("Forward: ")
printForward(circularArray,8,5)
print("Backward: ")
printBackward( circularArray,8,5)
print("Backward.2: ")
backwardIteration( circularArray,8,5)