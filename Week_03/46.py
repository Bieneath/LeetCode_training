class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        ret = []
        l = len(nums)
        def dfs(curr, rest):
            if l == len(curr):
                ret.append(curr)
                return
            for i in range(len(rest)):
                dfs(curr + [rest[i]], rest[:i] + rest[i+1:])
        # main
        dfs([], nums)
        return ret