import sys
import random
 
A = 31
PRIME = 27644437
SIZE = 10 ** 4
 
def str_hash(A, P, M, x):
    res = 0
    for i in x:
        res = (A * res + ord(i)) % P
    return res % M
 
 
class HashTable:
    
    def __init__(self):
        self.lst = [[] for i in range(SIZE)]
        
    def get(self, key):
        ind = str_hash(A, PRIME, SIZE, key)
        for i in range(len(self.lst[ind])):
            if self.lst[ind][i][0] == key:
                return [i, self.lst[ind][i][1]]
        return [-1, 'none']
    
    def put(self, key, val):
        ind = str_hash(A, PRIME, SIZE, key)
        get_val = self.get(key)
        if  get_val[0] == -1:
            self.lst[ind].append([key, val])
        else:
            self.lst[ind][get_val[0]][1] = val 
            
    def delete(self, key):
        get_val = self.get(key)
        if get_val[0] != -1:
            ind = str_hash(A, PRIME, SIZE, key)
            self.lst[ind].pop(get_val[0])
            
            
            
data = sys.stdin.buffer.readlines()
res = []
hash_table = HashTable()
 
for i in range(len(data)):
        cmd = data[i].split()
        command = cmd[0].decode()
        val = list(map(lambda x: x.decode(), cmd[1:]))
        if command == 'put':
            hash_table.put(val[0], val[1])
        elif command == 'delete':
            hash_table.delete(val[0])
        else:
            res.append(str(hash_table.get(val[0])[1]))    
            
sys.stdout.buffer.write('\n'.join(res).encode())