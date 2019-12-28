import ipdb

dbg = ipdb.set_trace


from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.cap = capacity        
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():   
            v = self.cache.pop(key)
            self.cache[key] = v
            return self.cache[key]
        else:
            return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache.keys():
            return
        else:
            if len(self.cache.keys()) >= self.cap:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value
            return


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    cache = LRUCache(2)
    dbg()
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       # returns 1
    cache.put(3, 3);    # evicts key 2
    cache.get(2);       # returns -1 (not found)
    cache.put(4, 4);    # evicts key 1
    cache.get(1);       # returns -1 (not found)
    cache.get(3);       # returns 3
    cache.get(4);       # returns 4

