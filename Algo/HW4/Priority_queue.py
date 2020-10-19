import sys
import math
 
 
class Heap:
    
    def __init__(self):
        self.lst = []
        self.size = 0
        self.oper = 0     
    
    def sift_up(self, i):
        while (i > 0) & (self.lst[i] < self.lst[(i - 1) // 2]):
                self.lst[i], self.lst[(i - 1) // 2] = self.lst[(i - 1) // 2], self.lst[i]
                i = (i - 1) // 2
        
    def insert(self, value):
        self.oper += 1
        self.lst.append([value, self.oper])
        self.size += 1
        i = self.size - 1
        if self.size != 1:  
            self.sift_up(i)
                    
    def extract_min(self):
        INF = math.inf
        self.oper += 1
        if self.size == 0:
            return '*'
        
        self.lst[0], self.lst[self.size - 1] = self.lst[self.size - 1], self.lst[0]
        min_el = self.lst.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            cur = self.lst[i]
            left = self.lst[2 * i + 1]
            
            if 2 * i + 2 != self.size:
                right = self.lst[2 * i + 2]
            else:
                right = [INF]
                
            if (left[0] < cur[0]) & (left[0] < right[0]):
                self.lst[i], self.lst[2 * i + 1] = self.lst[2 * i + 1], self.lst[i]
                i = 2 * i + 1
            elif (right[0] < cur[0]) & (right[0] <= left[0]):
                self.lst[i], self.lst[2 * i + 2] = self.lst[2 * i + 2], self.lst[i]
                i = 2 * i + 2
            else:
                break
                
        return str(min_el[0]) + ' ' + str(min_el[1])
    
    def decrease_key(self, operation, value):
        self.oper += 1
        for i in range(self.size):
            if self.lst[i][1] == operation:
                self.lst[i][0] = value
                self.sift_up(i)   
                break
 
priority_queue = Heap()
 
while True:
        line = sys.stdin.readline().split(' ')
        if line[0] == '':
            break
        if line[0] == 'push':
            priority_queue.insert(int(line[1]))
        elif line[0] == 'decrease-key':
            priority_queue.decrease_key(int(line[1]), int(line[2]))
        else:
            sys.stdout.write(priority_queue.extract_min() + '\n') 
    