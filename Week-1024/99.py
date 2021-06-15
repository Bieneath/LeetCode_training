# Morris中序遍历图解 https://leetcode-cn.com/problems/recover-binary-search-tree/solution/yi-wen-zhang-wo-morrisbian-li-suan-fa-by-a-fei-8/
# 这题的代码非常非常优秀，将中序遍历前后比较融入进了Morris中序遍历中。建议多练习几次morris遍历。
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur, nodes, pre = root, [], TreeNode(float('-inf'))
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur: # 不停循环直到找到mostRight节点为止
                    temp = temp.right
                if not temp.right:
                    temp.right, cur = cur, cur.left
                    continue # 这个continue前往别漏了；这里是cur能去cur.left的情况，下面是cur左边没有节点或者cur左边遍历完的情况，cur要去cur.right
                temp.right = None
            if pre.val > cur.val: nodes += [pre, cur]
            pre, cur = cur, cur.right
        nodes[0].val, nodes[-1].val = nodes[-1].val, nodes[0].val