class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ss = sum(set(nums))
        return [sum(nums) - ss, sum(range(1, len(nums)+1)) - ss]