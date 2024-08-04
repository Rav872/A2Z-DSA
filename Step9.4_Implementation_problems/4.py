# Implement LRU cache

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):

        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= capacity:
            self.cache.popitem(last=False)  #Remove first item from dictionary means last used
        self.cache[key] = value

capacity = 3

lru = LRUCache(capacity)

lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
print(lru.get(1))  # Should print 1, as key 1 is in the cache
lru.put(4, 4)      # This will evict key 2, as it is the least recently used
print(lru.get(2))
print(lru.get(3))

