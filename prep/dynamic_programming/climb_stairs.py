class Solution(object):
    def getCost(self, step, cost, memo):
        if(step >= len(cost)-1): return 0
        else:
            if(step in memo): return memo[step]
            memo[step] = min(cost[step]+self.getCost(step+1, cost, memo), 
                cost[step+1]+self.getCost(step+2, cost, memo))
            return memo[step]
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return self.getCost(0, cost, {})
a = Solution()
print(a.minCostClimbingStairs([10, 15, 20]))
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))