class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        for index in range(len(numbers)):
            if target-numbers[index] in nums:
                return [nums[target-numbers[index]]+1, index+1]
            else:
                nums[numbers[index]] = index
        return
        