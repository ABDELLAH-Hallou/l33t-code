from collections import defaultdict
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value=value
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = defaultdict(Node)
        self.new = Node(0,0)
        self.old = Node(0,0)

        self.new.prev, self.old.next = self.old, self.new

    def insert(self,node:Node):
        node.next = self.new
        node.prev = self.new.prev
        self.new.prev.next = node
        self.new.prev = node
        
    def remove(self,node:Node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        else:
            node = self.items[key]
            self.remove(node)
            self.insert(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.remove(self.items[key])
        node = Node(key,value)
        self.insert(node)
        self.items[key]=node
        if len(self.items) > self.capacity:
            lru = self.old.next
            self.remove(lru)
            del self.items[lru.key]

# Runtime : 582 ms 
# Memory : 78.5 MB