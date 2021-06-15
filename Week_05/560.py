class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 参考: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example 的解题思路
        dic = {0: 1}
        ret, acc = 0, 0
        for n in nums:
            acc += n
            ret += dic.get(acc - k, 0)
            dic[acc] = dic.get(acc, 0) + 1
        return ret