"""
LinkedList
Node - [Done]
LinkedList - [Done]
Append - [Done]
Length - [Done]
Print - [Done]
Insert in head - [Done]
Insert using position - [Done]
Indexing - [Done]
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

    #inserting from head
    def insert_from_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n+=1

    #insert using position
    def insert(self, pos, value):
        if pos < 0:
            raise Exception("Negative indexing on next version")
        if pos >= self.n:
            raise Exception("Index out of range")
        if pos == 0:
            self.insert_from_head(value)
            self.n+=1
        else:
            new_node = Node(value)
            curr = self.head
            i = 1
            while curr != None and i < self.n:
                if i == pos:
                    break
                curr = curr.next
                i+=1
            new_node.next = curr.next
            curr.next = new_node
            self.n+=1

    #indexing 
    def __getitem__(self, pos):
        if pos < 0:
            pos = self.n+pos
            if pos < 0:
                raise Exception("Index out of range")
        if pos >= self.n:
            raise Exception("Index out of range")
        if 0 <= pos < self.n:
            curr = self.head
            i = 0
            while curr != None and i < self.n:
                if i == pos:
                    return curr.data
                curr = curr.next
                i+=1
