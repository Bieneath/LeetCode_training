# 这题用divide and conquer方法解决最佳而且也最巧妙 
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31495/Should-be-6-Liner
from itertools import product
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if 0 == n: return []
        def divid_and_conquer(start, end):
            if start > end: return [None] # 这里一定要返回[None]，因为之后要用None构建树
            ret = []
            for cur in range(start, end+1):
                left = divid_and_conquer(start, cur-1) # 左侧节点组成的所有树根节点集合
                right = divid_and_conquer(cur+1, end) # 右侧节点组成的所有树根节点集合
                for le, ri in product(left, right): # 从左右侧的所有根节点中遍历取点构成新的树
                    ret.append(TreeNode(val=cur, left=le, right=ri))
            return ret
        return divid_and_conquer(1, n)