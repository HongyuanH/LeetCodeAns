from imports import *

class Solution:
    """ 
    Runtime: 1060 ms, faster than 70.66% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 25.2 MB, less than 54.73% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Reduced size of the dp array.
        """
        dp = 0
        lowest = prices[0]
        for n in range(1, len(prices)):
            price = prices[n]
            dp = max(dp, price-lowest)
            lowest = min(price, lowest)
        return dp

    def maxProfitDp(self, prices: List[int]) -> int: 
        """
        Sub-problem:
            * Find max profit for the past n-1 days
        Notes:
            * Because only dp[n-1] is used we don't actually need an array.
        Recurrence formula:
            * dp[i] = max(dp[j], profit)
        """
        dp = [0] * len(prices)
        lowest = prices[0]
        for n in range(1, len(prices)):
            price = prices[n]
            dp[n] = max(dp[n-1], price-lowest)
            lowest = min(price, lowest)
        return dp[-1]

if __name__ == "__main__": 
    print(Solution().maxProfit([7,1,5,3,6,4]))