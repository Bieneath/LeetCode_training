class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        explore = find_0 = 0
        for explore in range(len(nums)):
            if nums[explore] != 0:
                nums[explore], nums[find_0] = nums[find_0], nums[explore]
            if nums[find_0] != 0:
                find_0 += 1