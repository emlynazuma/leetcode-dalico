class LRUCache:

    def __init__(self, capacity: int):
        self.c = {}
        self.i = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        res = -1
        if key in self.c:
            res = self.c[key]
            self.i.remove(key)
            self.i.append(key)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.c:
            self.i.remove(key)
        self.i.append(key)
        self.c[key] = value
        if len(self.i) > self.capacity:
            r_key = self.i.pop(0)
            self.c.pop(r_key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
