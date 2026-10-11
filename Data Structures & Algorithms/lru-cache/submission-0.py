class LinkedList:
    def __init__ (self, value = None, key = None, next = None, prev = None):
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.hashmap = {}

        self.start = LinkedList()
        self.end = LinkedList()

        self.start.next = self.end
        self.end.prev = self.start
        

    def get(self, key: int) -> int:

        if key in self.hashmap:
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            temp = self.end.prev
            temp.next = node
            self.end.prev = node
            node.prev = temp
            node.next = self.end

            return node.value

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        node = LinkedList(value, key)
         
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev

            temp = self.end.prev
            temp.next = node
            self.end.prev = node
            node.prev = temp
            node.next = self.end

        else:
            self.hashmap[key] = node

            temp = self.end.prev
            temp.next = node
            self.end.prev = node
            node.prev = temp
            node.next = self.end
        
        if len(self.hashmap) > self.capacity:
            node = self.start.next
            self.start.next = node.next
            node.next.prev = self.start

            del self.hashmap[node.key]
        
