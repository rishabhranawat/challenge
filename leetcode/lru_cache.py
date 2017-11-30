class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.qu = []
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key in self.cache): 
            if(key in self.qu):
                self.qu.remove(key)
                self.qu.append(key)
            else:
                self.qu.append(key)
            return self.cache[key]
        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if(key not in self.cache and len(self.cache) == self.capacity):
            counter = 0
            lrused = self.qu[counter]
            while(lrused not in self.cache):
                counter += 1
                lrused = self.qu[counter]
            del self.cache[lrused]
            self.qu.remove(lrused)
        self.cache[key] = value
        if(key in self.qu):
            self.qu.remove(key)
        self.qu.append(key)