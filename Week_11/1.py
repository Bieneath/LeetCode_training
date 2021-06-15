class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ret = None
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dic:
                ret = [dic[diff], i]
                break
            dic[v] = i
        return ret