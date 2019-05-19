class Solution(object):
    def checkIfValidState(self, piles):
        for each in piles:
            if(each > 0):
                return False
        return True
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        current_piles = [x for x in piles]
        smallest = min(piles)
        n = len(current_piles)
        not_found = True
        while(not_found):
            hours_used = 0
            i = 0
            while(hours_used < H):
                index = i % n
                current = current_piles[index]
                current_piles[index] -= smallest
                if(current_piles[index] < 0):
                    current_piles[index] = 0
                
                if(current > 0):
                    hours_used += 1
                i += 1
            found = self.checkIfValidState(current_piles)
            if(not found):
                current_piles = [x for x in piles]
                smallest = smallest + 1
            else:
                return smallest
        return smallest
            
           
        
a = Solution()
print(a.minEatingSpeed([3,6,7,11], 8))
print(a.minEatingSpeed([30,11,23,4,20], 5))
print(a.minEatingSpeed([30,11,23,4,20], 6))
