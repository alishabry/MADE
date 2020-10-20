import sys
import random
 
A = 31
PRIME = 27644437
SIZE = 10 ** 6
NONE_STR = 'none'
 
 
def str_hash(A, P, M, x):
    res = 0
    for i in x:
        res = (A * res + ord(i)) % P
    return res % M
 
 
class Node:
    def __init__(self, key = None, value = None, next_val = None, prev_val = None):
        self.key = key
        self.value = value
        self.next_val = next_val
        self.prev_val = prev_val
 
 
class HashTable:
 
    def __init__(self):
        self.lst = [[] for i in range(SIZE)]
        self.last = None
 
    def get_index_value(self, key):
        ind = str_hash(A, PRIME, SIZE, key)
        for i in range(len(self.lst[ind])):
            if self.lst[ind][i].key == key:
                return [i, self.lst[ind][i]]
        return [-1, NONE_STR]
 
    def get_val(self, key):
        val = (self.get_index_value(key)[1])
        if val == NONE_STR:
            return val
        return val.value
 
    def put(self, key, val):
        isin = self.get_index_value(key)
        ind = str_hash(A, PRIME, SIZE, key)
        if isin[0] == -1:
            new_node = Node(key=key, value=val, prev_val=self.last)
            self.lst[ind].append(new_node)
            if self.last is not None:
                self.last.next_val = new_node
            self.last = new_node
        else:
            self.lst[ind][isin[0]].value = val
 
    def delete(self, key):
        isin = self.get_index_value(key)
        if isin[0] != -1:
            ind = str_hash(A, PRIME, SIZE, key)
            prev_value = self.lst[ind][isin[0]].prev_val
            next_value = self.lst[ind][isin[0]].next_val
            
            if (prev_value is None) & (next_value is None):
                self.last = None
            else:
                if prev_value is not None:
                    prev_value.next_val = next_value
                if next_value is not None:
                    next_value.prev_val = prev_value
                else:
                    self.last = prev_value
            del self.lst[ind][isin[0]]
 
    def get_prev_next(self, key):
        isin = self.get_index_value(key)
        if isin[0] != -1:
            ind = str_hash(A, PRIME, SIZE, key)
            return self.lst[ind][isin[0]]
        return NONE_STR
 
    def get_next(self, key):
        next_value = self.get_prev_next(key)
        if (next_value == NONE_STR):
            return next_value
        if (next_value.next_val is None):
            return NONE_STR
        return next_value.next_val.value
 
    def get_prev(self, key):
        prev_value = self.get_prev_next(key)
        if (prev_value == NONE_STR):
            return prev_value
        if (prev_value.prev_val is None):
            return NONE_STR
        return prev_value.prev_val.value
 
    
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
    elif command == 'get':
        res.append(hash_table.get_val(val[0]))
    elif command == 'prev':
        res.append(hash_table.get_prev(val[0]))
    else:
        res.append(hash_table.get_next(val[0]))
 
sys.stdout.buffer.write('\n'.join(res).encode())