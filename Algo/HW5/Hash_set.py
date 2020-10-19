import random
import sys 
 
 
def hash_func(A, P, M, x):
    return ((A * x) % P) % M
    
PRIME = 27644437
DEL_ELEMENT = 'rip'
SIZE = 10 ** 6
A_RANGE = [100, 1000]
 
 
class HashTable:
    
    def __init__(self):
        self.size = 0
        self.capacity = 2 * SIZE
        self.lst = [None] * self.capacity
        self.A = random.randint(A_RANGE[0], A_RANGE[1])
    
    def rehash(self):
        self.A = random.randint(A_RANGE[0], A_RANGE[1])
        self.capacity *= 2
        newLst = self.capacity * [None]
        for i in self.lst:
            if i != DEL_ELEMENT:
                self.insert(newLst, i)
        self.lst = newLst  
        
    def insert(self, lst, x):
        i = hash_func(self.A, PRIME, self.capacity, x)   
        while (lst[i] != None) & (lst[i] != DEL_ELEMENT):
            if lst[i] == x:
                self.size -= 1
                return 0
            i = (i + 1) % self.capacity
        lst[i] = x
        
    def put(self, x):
        if self.size == self.capacity:
            self.rehash()
        self.insert(self.lst, x)
        self.size += 1
        
    def delete(self, x):
        i = hash_func(self.A, PRIME, self.capacity, x) 
        while self.lst[i] != None:
            if self.lst[i] == x:
                self.lst[i] = DEL_ELEMENT
                self.size -= 1
                break
            i = (i + 1) % self.capacity
         
    def exsists(self, x):
        i = hash_func(self.A, PRIME, self.capacity, x) 
        while self.lst[i] != None:
            if self.lst[i] == x:
                return 'true'
            i = (i + 1) % self.capacity
        return 'false'
 
    
data = sys.stdin.buffer.readlines()
hash_table = HashTable()
res = []
 
for i in range(len(data)):
        cmd = data[i].split()
        command = cmd[0].decode()
        val = int(cmd[1])
        if command == 'insert':
            hash_table.put(val)
        elif command == 'delete':
            hash_table.delete(val)
        else:
            res.append(hash_table.exsists(val))
            
sys.stdout.buffer.write('\n'.join(res).encode())