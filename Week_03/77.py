# 一般递归算法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n+1)]
        ret = []
        def helper(path):
            if len(path) >= k:
                ret.append(path)
                return
            last = path[-1] if path else 0
            for d in nums[last:]:
                helper(path + [d])
        # main
        helper([])
        return ret

# 循环算法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [c + [i] for c in combs for i in range(c[-1]+1 if c else 1, n+1)]
            # combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
            # temp = []
            # for c in combs:
            #     if c:
            #         for i in range(1, c[0]):
            #             temp.append([i] + c)
            #     else:
            #         for i in range(1, n+1):
            #             temp.append([i])
            #     combs = temp
            # temp = []
            # for c in combs:
            #     if c:
            #         for i in range(c[-1]+1, n+1):
            #             temp.append(c + [i])
            #     else:
            #         for i in range(1, n+1):
            #             temp.append([i])
            #     combs = temp
        return combs