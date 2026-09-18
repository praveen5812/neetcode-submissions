class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                profit = prices[i] - min_buy
                if profit > max_profit:
                     max_profit = profit
        return max_profit



#   prices = [10,1,5,6,7,1],max_profit = 0, min_buy = price[0] = 10 and compare it with next price[1] 
#if price[1] is smaller than price[0] update min_buy = 1 
#and move right pointer to the right side price[2] = 5 if price [2] is greater then subtract it with price[1] in variable profit
# and update it with the maximum max_profit if profit > max_profit then max_profit = profit