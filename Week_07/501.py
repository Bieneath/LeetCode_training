from collections import defaultdict
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        ret = []
        dd = defaultdict(int)
        # 先遍历二叉树获得val与count对应的字典
        def dfs(root):
            if not root: return
            dd[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # 对字典进行排序，取出个数最多的val
        items = sorted(dd.items(), key=lambda x:x[1], reverse=True)
        for i, v in enumerate(items):
            if not ret: 
                ret.append(v[0])
            elif items[i][1] < items[i-1][1]: 
                break
            else:
                ret.append(v[0])
        return ret