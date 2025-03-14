class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # store lowest, if not lower, compare to to the rest of array
        buy = prices[0]
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
            elif i-buy > profit: # miss the (-buy) in this line
                profit = i - buy

        return profit 