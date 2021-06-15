class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        check = sorted(nums)
        return [check.index(n) for n in nums]