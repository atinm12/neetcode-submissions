class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        second = {}
        for num in nums:
            if num in second: return True
            second[num] = 1
        return False
        