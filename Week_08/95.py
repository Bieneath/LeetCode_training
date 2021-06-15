# 这题用divide and conquer方法解决最佳而且也最巧妙
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if 0 == n: return []
        def helper(start, end):
            if start > end:
                return [None]
            nodes = []
            for n in range(start, end+1):
                left = helper(start, n-1)
                right = helper(n+1, end)
                for le in left:
                    for ri in right:
                        root = TreeNode(n)
                        root.left, root.right = le, ri
                        nodes.append(root)
            return nodes
        return helper(1, n)