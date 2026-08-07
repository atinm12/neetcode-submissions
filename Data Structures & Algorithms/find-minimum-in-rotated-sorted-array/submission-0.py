class Solution:
    def findMin(self, nums: List[int]) -> int:
        beginning = 0
        end = len(nums) - 1
        lowest = None
        while beginning <= end:
            middle = (beginning + end) // 2
            if nums[middle] - nums[end] > 0:
                if lowest == None: 
                    lowest = nums[middle]
                else: 
                    if nums[middle] < lowest: lowest = nums[middle]
                beginning = middle + 1
            else:
                if lowest == None:
                    lowest = nums[middle]
                else: 
                    if nums[middle] < lowest: lowest = nums[middle]
                end = middle - 1
        return lowest