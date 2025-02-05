## 08.05.2024
# Creating stack using linkedlist
"""
Stack operations:
creating node - [Done]
creating stack - [Done]
push - To insert an element to last - [Done]
pop - To remove/out from the last (LIFO) concept - [Done]
peak - To retreive data of the top - [Done]
is_empty - to check the stack is empty - [Done]
length - to get the size of the stack - [Done]
traverse - to print the elements in the stack - [Done]
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty!!"
        data = self.top.data
        self.top = self.top.next
        return data

    def peak(self):
        if self.is_empty():
            return "Stack is empty!!"
        return self.top.data

    def __len__(self):
        size = 0
        if self.is_empty():
            return size
        curr = self.top
        while curr != None:
            size+=1
            curr = curr.next
        return size

    def __str__(self):
        result = ""
        curr = self.top
        while curr != None:
            result = result+str(curr.data)+", "
            curr = curr.next
        return "[ "+result[:-2]+" ]"
