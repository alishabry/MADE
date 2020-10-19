class ExpandingArray:
    
    def __init__(self, n):
        self.lst = n * [0]
        self.size = 0
        self.capacity = n
    
    def get(self, i):
        if (i < 0) or (i >= self.size):
            return None
        return self.lst[i]    
    
    def ensureCapacity(self):
        ENS = 2
        self.capacity *= ENS
        newLst = self.capacity * [0]
        for i in range(self.size):
            newLst[i] = self.lst[i]
        self.lst = newLst   
    
    def add(self, new):
        if self.size == self.capacity:
            self.ensureCapacity()            
        self.lst[self.size] = new
        self.size += 1    
        
    def erase(self):
        ERS = 4
        if self.size <= self.capacity // ERS:
            self.decreaseCapacity()            
        self.lst[self.size - 1] = 0
        self.size -= 1
          
    def decreaseCapacity(self):
        self.capacity //= 2
        newLst = self.capacity * [0]
        for i in range(self.size):
            newLst[i] = self.lst[i]
        self.lst = newLst
        
q = input()
stack = ExpandingArray((len(q) + 1) // 2)
 
for i in q.split(' '):
    if i.isdigit():
        stack.add(int(i))
    else:
        if i == '+':
            val = stack.get(stack.size - 1) + stack.get(stack.size - 2)
        elif i == '*':
            val = stack.get(stack.size - 1) * stack.get(stack.size - 2)
        elif i == '-':
            val = stack.get(stack.size - 2) - stack.get(stack.size - 1)  
        stack.erase()
        stack.erase()
        stack.add(val)
    
print(stack.get(0))