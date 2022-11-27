class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyTime = True
        profit = 0
        i = 0
        last_buy = 0
        while (i < len(prices)-1):
            if (buyTime):
                if prices[i] > prices[i+1]:
                    i = i + 1
                elif prices[i] < prices[i+1]:
                    buyTime = False
                    profit = profit - prices[i]
                    last_buy = prices[i]
                    i = i + 1
                else:
                    i = i+1
            else:
                if prices[i] > prices[i+1]:
                    buyTime = True
                    profit = profit + prices[i]
                else:
                    i = i+1
        if not buyTime:
            if prices[len(prices)-1] >= prices[len(prices)-2]:
                profit = profit + prices[len(prices)-1]
            else:
                profit = profit + last_buy
        return profit