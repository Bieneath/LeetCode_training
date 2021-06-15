class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = i = 0
        while i < len(nums):
            if not i or (nums[i] == nums[i-1] and count < 2):
                count += 1
                i += 1
            elif nums[i] != nums[i-1]:
                count = 1
                i += 1
            elif nums[i] == nums[i-1] and count >= 2:
                nums.pop(i)
        return len(nums)