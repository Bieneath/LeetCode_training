class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        ret = []
        nums = [_ for _ in range(1, 10)]
        def dfs(cur_list, rest):
            if sum(cur_list) == target:
                if len(cur_list) == k:
                    ret.append(cur_list)
                return
            for i in range(len(rest)):
                if rest[i] > target: break
                if not cur_list or rest[i] > cur_list[-1]:
                    dfs(cur_list + [rest[i]], rest[:i] + rest[i+1:])
        dfs([], nums)
        return ret