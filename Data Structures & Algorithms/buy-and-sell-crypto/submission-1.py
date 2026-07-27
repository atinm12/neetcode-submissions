class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 1
        highest = 0
        window = [prices[0]]
        while index < len(prices):
            if prices[index] < min(window):
                if max(window) - min(window) > highest:
                    highest = max(window) - min(window)
                window = [prices[index]]
            else: 
                window.append(prices[index])
                if max(window) - min(window) > highest:
                    highest = max(window) - min(window)
            index += 1
        return highest
            

        