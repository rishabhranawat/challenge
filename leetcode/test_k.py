# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
The idea was to use a binary index tree
to keep track of the cumulative score of
whether a flower has bloomed or not.

The BIT updates in logN time and thus,
the required complexity could be achieved.
'''

class BinaryIndexTree(object):
    def __init__(self, nums):
        self.nums = [0]*(len(nums))
        self.bit = [0]*(len(nums)+1)
    
    def parent(self, index):
        complement = (~index)+1
        return index - (complement&index)
    
    def next(self, index):
        complement = (~index)+1
        return index + (complement&index)
    
    def update(self, index, val):
        diff = val-self.nums[index]
        self.nums[index] = val
        
        next = index+1
        while(next < len(self.bit)):
            self.bit[next] += diff
            next = self.next(next)
    
    def cumulate(self, index):
        prev = index + 1
        cumu = 0
        while(prev > 0):
            cumu += self.bit[prev]
            prev = self.parent(prev)
        return cumu

def check(bloomed, K):
    for i in range(0, len(bloomed), 1):
        print(bloomed)
        if(bloomed[i] == 0): continue
        for j in range(i+1, len(bloomed),1):
            if(bloomed[j] == 1): continue
            elif(j-i == K): return j
    return -1
        

def solution(P, K):
    # write your code in Python 3.6
    n = len(P)
    bloomed = [0]*n
    bit = BinaryIndexTree(bloomed)
    
    tracker = {}
    m = -1
    for i in range(0, n, 1):
        rose = P[i]-1
        bloomed[rose] = 1
        m = max(m, check(bloomed, K))
        print(m)
        # bit.update(rose, 1)
        # current_cumu = bit.cumulate(rose)
        # if(rose+K+1 in tracker):
        #     score = bit.cumulate(rose+K+1)-current_cumu
        #     if(score == 1):
        #         m = max(m, i+1)
        # if(rose-K-1 in tracker):
        #     score = current_cumu - bit.cumulate(rose-K-1)
        #     if(score == 1):
        #         m = max(m, i+1)
        # tracker[rose] = True
        
    return m
            
        
            
        
a = solution([3, 1, 5, 4, 2], 1) 
print(a)
# a = solution([1, 3, 2], 1) 
# print(a)
# a = solution([1, 2, 3], 1)
print(a) 
        