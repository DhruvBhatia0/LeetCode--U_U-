class Solution:
    
    def climbcount (self, n, store):
        #for some n, return ways to get to it
        if n < 2:
            store[0] = 1
            store[1] = 1
            return 1, store
        
        if n-1 in store.keys():
            previous = store[n-1]
        else:
            previous, store = self.climbcount(n-1, store)
        
        if n-2 in store.keys():
            previous2 = store[n-2]
        else:
            previous2, store = self.climbcount(n-2, store)
        
        store[n] = previous + previous2
        
        return store[n], store
        
        
    def climbStairs(self, n: int) -> int:
        store = {}
        
        count, store = self.climbcount(n, store)
        
        return count