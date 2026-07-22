class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        index = 0
        for num in nums:
            if target-num in past:
                return [past[target-num], index]
            else:
                past[num] = index
            index += 1
        return 