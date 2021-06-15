# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
# 这题还是能用前缀和来解，不过不太容易想到
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1} # 首先需要一个记录累加和第一次出现下表位置的字典
        ret = cur = 0 # 然后需要一个返回值ret以及一个记录当前累加值的cur
        for i, n in enumerate(nums):
            if n: cur += 1 # 当元素为1时候+1，元素为0时候-1
            else: cur -= 1
            pos.setdefault(cur, i) # pos只记录cur第一次出现的下标位置！
            ret = max(ret, i - pos[cur])
        return ret