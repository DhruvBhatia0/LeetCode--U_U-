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
                    continue
                elif prices[i] < prices[i+1]:
                    print(i)
                    buyTime = False
                    profit = profit - prices[i]
                    last_buy = prices[i]
                    i = i + 1
                    continue
                else:
                    i = i+1
            else:
                if prices[i] > prices[i+1]:
                    print(i)
                    buyTime = True
                    profit = profit + prices[i]
                    continue
                else:
                    i = i+1
                    continue
        if not buyTime:
            if prices[len(prices)-1] >= prices[len(prices)-2]:
                profit = profit + prices[len(prices)-1]
            else:
                profit = profit + last_buy
        return profit