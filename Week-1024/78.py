# bitmask + 哈希表; 参考1178的bitmask+位运算求子集方法 https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/372145/Python-Bit-manipulation-detailed-explanation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 数字（二进制位）转list函数，比如数组[1, 2, 3]，0、1、2下标位置的数字都存在，那么转为bitmask形式就是111，十进制表示就是7
        # bit2list就是这个过程的反向过程，当前n=7，二进制位111，即0、1、2位置数字都有，返回[1, 2, 3]这个列表
        def bit2list(n):
            ret = []
            idx = 0
            while n:
                if n&1:
                    ret.append(nums[idx])
                n >>= 1
                idx += 1
            return ret
        ret = []
        # 将不同位置的字符对应一个二进制位置1，比如[1, 2]->11，[1, 2, 3]->111
        base, one = 0, 1
        for _ in range(len(nums)):
            base += one
            one <<= 1
        # 二进制遍历所有子集的方法，比如base=11，其二进制子集有01与10
        mask = base
        while mask:
            ret.append(bit2list(mask))
            mask = (mask - 1) & base
        return ret + [[]]

# # 通用递归+回溯算法
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         def dfs(i, path):
#             ret.append(path)
#             for j in range(i, len(nums)):
#                 dfs(j+1, path + [nums[j]]) # 这里注意要写成j+1!
#         dfs(0, [])
#         return ret

# # 使用动态规划
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         dp = [[]]
#         for n in nums:
#             dp += [it + [n] for it in dp]
#         return dp

# # 使用combinations方法
# from itertools import combinations
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         l = len(nums)
#         ret = []
#         for i in range(l+1):
#             temp = list(map(list, combinations(nums, i)))
#             ret += temp
#         return ret