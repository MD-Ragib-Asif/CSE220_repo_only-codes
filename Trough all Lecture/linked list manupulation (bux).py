#insert function

def insert(head, size, elem, index):

    if(index<0 or index>size):

        raise Exception("Invalid index")

    newNode = Node(elem, None)

    if (index==0):

        newNode.next = head

        head = newNode

    else:

        pred = nodeAt(index-1)

        newNode.next = pred.next

        pred.next = newNode

    return head




#remove function

def remove(head, size, index):

    if(index<0 or index>=size):

        raise Exception("Invalid index")

    removedNode = None

    if (index==0):

        removedNode = head

        head = head.next

    else:

        pred = nodeAt(index-1)

        removedNode = pred.next

        pred.next = removedNode.next

    removedNode.element = None

    removedNode.next = None

    return head