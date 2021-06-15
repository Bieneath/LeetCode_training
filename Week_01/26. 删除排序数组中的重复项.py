class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        del nums[j+1:]
        return j+1