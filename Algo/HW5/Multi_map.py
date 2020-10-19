import sys
import random
 
 
KEYS_SIZE = 10 ** 5
VALS_SIZE = 10 ** 2
A = 31
PRIME = 127
 
    
def str_hash(A, P, M, x):
    res = 0
    for i in x:
        res = (A * res + ord(i)) % P
    return res % M
 
    
class HashTable:  
    
    def __init__(self):
        self.lst = [[] for i in range(KEYS_SIZE)]
    
    def get_hashes(self, key, val):
        return [str_hash(A, PRIME, KEYS_SIZE, key), str_hash(A, PRIME, VALS_SIZE, val)]
        
    def get_ind(self, key, val):
        hashes = self.get_hashes(key, val)
        for i in range(len(self.lst[hashes[0]])):
            if (self.lst[hashes[0]][i][0] == key):
                for j in range(len(self.lst[hashes[0]][i][1][hashes[1]])):
                    if (self.lst[hashes[0]][i][1][hashes[1]][j] == val):
                        return [i, j]
        return [-1]
    
    def get(self, key):
        hash_key = str_hash(A, PRIME, KEYS_SIZE, key)
        cnt = 0
        vals = []
        for i in range(len(self.lst[hash_key])):
            if (self.lst[hash_key][i][0] == key):
                values = sum(self.lst[hash_key][i][1], [])
                return str(len(values)) + ' ' + ' '.join(values)
        return '0'
    
    def get_ind_key(self, key):
        hash_key = str_hash(A, PRIME, KEYS_SIZE, key)
        for i in range(len(self.lst[hash_key])):
            if (self.lst[hash_key][i][0] == key):
                return [i]
        return [-1]
                   
    def put(self, key, val):
        get_val = self.get_ind_key(key)
        hashes = self.get_hashes(key, val)
        if get_val[0] == -1:
            self.lst[hashes[0]].append([key, [[] for i in range(VALS_SIZE)]])
            self.lst[hashes[0]][-1][1][hashes[1]].append(val)
        else:
            get = self.get_ind(key, val)
            if get[0] == -1:
                self.lst[hashes[0]][get_val[0]][1][hashes[1]].append(val)
 
    def delete(self, key, val):
        get_val = self.get_ind(key, val)
        if get_val[0] != -1:
            hashes = self.get_hashes(key, val)
            del self.lst[hashes[0]][get_val[0]][1][hashes[1]][get_val[1]]
            
            
    def delete_all(self, key):
        get_val = self.get_ind_key(key)
        if get_val[0] != -1:
            hash_key = str_hash(A, PRIME, KEYS_SIZE, key)
            del self.lst[hash_key][get_val[0]]
            
            
            
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
            hash_table.delete(val[0], val[1])
        elif command == 'deleteall':
            hash_table.delete_all(val[0])
        else:
            res.append(hash_table.get(val[0]))    
sys.stdout.buffer.write('\n'.join(res).encode())