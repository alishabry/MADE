import sys
 
 
class CycleExpandingArray:
    
    def __init__(self, n):
        self.lst = n * [0]
        self.begin = 0
        self.end = None
        self.capacity = n
        self.size = 0
 
    def ensureCapacity(self):
        self.capacity *= 2
        newLst = self.capacity * [0]
        for i in range(self.size):
            newLst[i] = self.lst[self.begin]
            self.begin = (self.begin + 1) % (self.capacity // 2)
        self.lst = newLst
        self.begin = 0
        self.end = self.size
 
    def add(self, new):
        if self.end == None:
            self.lst[self.begin] = new
            self.end = 1
            self.size = 1
        else:
            if self.end == self.begin:
                self.ensureCapacity()  
            self.lst[self.end] = new
            self.end = (self.end + 1) % self.capacity 
            self.size += 1
            
    def erase(self): 
        elem = self.lst[self.begin]
        self.lst[self.begin] = 0
        self.begin = (self.begin + 1) % self.capacity 
        if self.size <= self.capacity // 4:
            self.decreaseCapacity()
        self.size -= 1
        if self.size == 0:
            self.end = None
        return elem
 
    def decreaseCapacity(self):
        self.capacity //= 2
        newLst = self.capacity * [0]
        for i in range(self.size):
            newLst[i] = self.lst[self.begin]
            self.begin = (self.begin + 1) % (self.capacity * 2)
        self.lst = newLst
        self.begin = 0
        self.end = self.size
        
n = int(sys.stdin.readline())
queue = CycleExpandingArray(2)
for i in range(n):
    operation = sys.stdin.readline().split(' ')
    if operation[0] == '+':
        queue.add(operation[1])
    else:
        sys.stdout.write(str(queue.erase()) + '\n')