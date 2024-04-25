"""
LinkedList
Node - [Done]
LinkedList - [Done]
Append - [Done]
Length - [Done]
Print - [Done]
"""
#creating a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    #append to the list
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(value)
        self.n+=1

    #length of the LL
    def __len__(self):
        return self.n

    #printing element
    def __str__(self):
        result = ""
        curr = self.head
        while curr != None:
            result = result+str(curr.data)+" -> "
            curr = curr.next
        return "[ " + result[:-4] + " ]"

    def __repr__(self):
        return self.__str__()
