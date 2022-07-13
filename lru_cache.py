class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


print("Initializing LRU Cache object...")
lru_obj = LRUCache(2)
print("PUT: (1, 1)")
lru_obj.put(1, 1)
print("PUT: (2, 2)")
lru_obj.put(2, 2)
print("GET: (1)")
print("Fetching from cache: " + str(lru_obj.get(1)))
print("PUT: (3, 3)")
lru_obj.put(3, 3)
print("GET: (2)")
print("Fetching from cache: " + str(lru_obj.get(2)))
print("PUT: (4, 4)")
lru_obj.put(4, 4)
print("GET: (1)")
print("Fetching from cache: " + str(lru_obj.get(1)))
print("GET: (3)")
print("Fetching from cache: " + str(lru_obj.get(3)))
print("GET: (4)")
print("Fetching from cache: " + str(lru_obj.get(4)))