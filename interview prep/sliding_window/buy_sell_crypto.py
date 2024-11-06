



# DP solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP


# main idea is to iterate through the prices and keep track of the minimum buy price
# we calculate the profit by subtracting the minimum buy price from the current price
# we update the maximum profit if the current profit is greater than the maximum profit
# we update the minimum buy price if the current price is less than the minimum buy price


# Sliding window solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if the left pointer is less than the right pointer, we calculate the profit
        # we move the left pointer to the right if the current price is less than the price at the left pointer
        # this means that we are making a loss (going down curve), so we move the left pointer to the right

        # we move the right pointer to the right if the current price is greater than the price at the left pointer
        # we update the maximum profit if the current profit is greater than the maximum profit
        left = 0
        right = 1
        maxP = 0
        while right < len(prices):
            # if the price at the left pointer is less than the price at the right pointer
            if prices[left] < prices[right]:
                # we calculate the profit
                profit = prices[right] - prices[left]
                # we update the maximum profit if the current profit is greater than the maximum profit
                maxP = max(maxP, profit)
            else:
                left = right
                # we move the left pointer to the right pointer
            right += 1
        return maxP
