"""
Very simple, same idea already built in OderedDict
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key)
        
        return self.store.get(key,-1)

        

    def put(self, key: int, value: int) -> None:
        # Update the key position
        if key in self.store:
            self.store.move_to_end(key)
        
        self.store[key] = value
        
        # Trim
        if len(self.store) > self.capacity:
            self.store.popitem(last= False)
        



