class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsdict = set(nums)
        highest = 0
        for num in nums:
            if num - 1 not in numsdict:
                length = 0
                while num + length in nums:
                    length += 1
                if length > highest:
                    highest = length
        return highest