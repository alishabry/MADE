import sys
 
 
class Node:
    
    def __init__(self, value = None, next_val = None):
        self.value = value
        self.next_val = next_val
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self, new_element):
        newNode = Node(value = new_element)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next_val = self.head
            self.head = newNode
        self.size += 1
       
    def pop(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_val
        self.size -= 1
                
            
class Stack:
    
    def __init__(self):
        self.list = LinkedList()
        self.min_list = LinkedList()    
        
    def insert(self, value):
        if self.list.size == 0:
            self.min_list.insert(value)   
        elif value <= self.min_list.head.value:
            self.min_list.insert(value) 
        self.list.insert(value)
        
    def pop(self):
        if self.list.head.value == self.min_list.head.value:
            self.min_list.pop()
        self.list.pop()
        
    def min_val(self):
        return self.min_list.head.value
             
 
n = int(sys.stdin.readline())
stack = Stack()
 
for i in range(n):
    oper = sys.stdin.readline().split(' ')
    if int(oper[0]) == 1:
        stack.insert(int(oper[1]))
    elif int(oper[0]) == 2:
        stack.pop()
    else:
        sys.stdout.write(str(stack.min_val()) + '\n')