from typing import List
#My solution is slower
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=0,1
        max_profit=0
        while(sell<len(prices) and buy < len(prices)-1):
            profit=prices[sell]-prices[buy]
            if profit > 0:
                max_profit=max(max_profit,profit)
                sell+=1
            else:
                buy+=1
                sell=buy+1
                
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=0,1
        max_profit=0
        while(sell<len(prices) and buy < len(prices)-1):
            profit=prices[sell]-prices[buy]
            if profit > 0:
                max_profit=max(max_profit,profit)
            else:
                buy=sell
            sell+=1
                
        return max_profit