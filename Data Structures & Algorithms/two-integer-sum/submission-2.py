class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = {}
        for i in range (len(nums)):
            if target - nums[i] in numlist:
                return [numlist[target-nums[i]], i]
            else:
                numlist[nums[i]] = i
        return