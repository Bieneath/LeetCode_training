# 并查集原理： https://leetcode-cn.com/problems/redundant-connection/solution/tong-su-jiang-jie-bing-cha-ji-bang-zhu-xiao-bai-ku/
# 代码实现： https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = ''.join(map(chr, range(1001)))
        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]
            tree = tree.replace(tree[u], tree[v])