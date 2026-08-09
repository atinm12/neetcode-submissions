class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range (len(nums)-1):
            left.append(left[len(left)-1] * nums[i])
        right = [1]
        nums = nums[::-1]
        for i in range (len(nums)-1):
            right.append(right[len(right)-1] * nums[i])
        right = right[::-1]
        final = []
        for i in range (len(right)):
            final.append(left[i] * right[i])
        return final

        