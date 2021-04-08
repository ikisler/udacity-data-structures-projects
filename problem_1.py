from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            capacity = 1 # Minimum capacity is at least 1

        # Initialize class variables
        self._data = OrderedDict()
        self._capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self._data.get(key)
        if value is None:
            return -1
        # By removing and re-adding the item, we push it to the bottom of the OrderedDict
        self._data.pop(key)
        self._data[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self._data) == self._capacity:
            # Have to clear our least used item
            self._data.popitem(last=False)
        self._data[key] = value

# Basic functionality tests
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))
# returns 1

print(our_cache.get(2))
# returns 2

print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Edge case: Cache size of 0 -- auto resets this to the minimum cache size of 1
our_cache = LRU_Cache(0)

our_cache.set(1, 1)
our_cache.set(2, 2);
print(our_cache.get(1))
# returns -1

# Edge case: Cache size not a number -- auto resets this to the minimum cache size of 1
our_cache = LRU_Cache("asdf")

our_cache.set(1, 1)
print(our_cache.get(1))
# returns 1

