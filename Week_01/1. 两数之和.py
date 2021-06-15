class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)): dic[nums[i]] = i
        for i in range(len(nums)):
            v = target - nums[i]
            if v in dic and i != dic[v]:
                return [i, dic[v]] 
        return None