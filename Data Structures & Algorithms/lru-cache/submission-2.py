class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

   
    
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0

        self.hashmap = {}

        self.start = Node()
        self.end = Node()

        self.start.next = self.end
        self.end.prev = self.start

    
    def get(self, key):
        if key not in self.hashmap:
            return -1
        
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])

        return self.hashmap[key].value
    
    def insert(self, node):
        self.end.prev.next = node
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev
    

    def put(self, key, value):

        if key in self.hashmap:
            self.remove(self.hashmap[key])
        else:
            self.length += 1
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)

        while self.length > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.hashmap[lru.key]
            self.length -= 1
