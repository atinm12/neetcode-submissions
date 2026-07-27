class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        left, right = 0, 0
        for i in range (1, len(prices)):
            if prices[i] < prices[left]:
                if prices[right] - prices[left] > highest:
                    highest = prices[right] - prices[left]
                left, right = i, i
                print(f'{i}, smaller, l = {left}, r = {right}, highest = {highest}')
            elif prices[i] > prices[right]:
                right = i
                if prices[right] - prices[left] > highest:
                    highest = prices[right] - prices[left]
                print(f'{i}, bigger, l = {left}, r = {right}, highest = {highest}')
        return highest