class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Add to front
        node.next = self.head.next 
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        return node.val 


    def put(self, key: int, value: int) -> None:
        # Remove od node if exists
        if key in self.cache:
            old_node = self.cache[key]
            old_node.prev.next = old_node.next
            old_node.next.prev = old_node.prev

        # Create and add new node
        node = Node(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.cache[key] = node

        # Evict LRU if needed
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            lru.prev.next = self.tail
            self.tail.prev = lru.prev
            del self.cache[lru.key]
        
        
