class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left, right = [1] * l, [1] * l
        for i in range(l-1):
            left[i+1] = left[i] * nums[i]
        for i in range(l-1, 0, -1):
            right[i-1] = right[i] * nums[i]
        return [x*y for x, y in zip(left, right)]