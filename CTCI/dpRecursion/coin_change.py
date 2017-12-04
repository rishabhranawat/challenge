class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        c = [float("inf")]*(amount+1)
        c[0] = 0
        for i in range(1, amount+1, 1):
            for j in range(0, len(coins), 1):
                denom = coins[j]
                if(i >= denom and c[i] > 1+c[i-denom]):
                    c[i] = 1 + c[i-denom]
        return (c[amount]) if(c[amount] != float("inf")) else -1
        
            


a = Solution()
print(a.coinChange([25, 10, 5, 1], 15))
print(a.coinChange([2], 11))