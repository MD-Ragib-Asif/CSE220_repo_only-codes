"""
Created on Tue Oct 27 22:37:02 2020

@author: SIFAT E JAHAN
"""
#------------------------------Node Class-----------------------------------#

from tkinter import N


class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def printNode(self):
        print(self.value, "-", self.next)


#------------------------------Linked List Class-----------------------------------#
class LinkedList:

    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            n= node.Node(i,None)
            if self.head is None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n


    def printList(self):
        n = self.head
        while n is not None:
            print(n.value)
            n = n.next


#------------------------------Tester Class-----------------------------------#

list1 = [1,2,3,4,5]
list2 = LinkedList(list1)

list2.printList()
