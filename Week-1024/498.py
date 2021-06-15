# 类似题目的通用解题思路：观察下标的排列(i,j)顺序:(0,0)|(0,1)(1,0)|(2,0)(1,1)(0,2)|(1,2)(2,1)|(2,2),会发现层|之间i+j相差1，因此可以先用i+j作为因子先做个粗排序，然后观察(2,0)(1,1)(0,2)这一段，当i+j是奇数时候，根据j从小到大排序，当i+j是偶数时候，根据i从小到大排序。因此完全可以用排序方法将下标先排号
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not any(matrix): return [] # 判断矩阵是否为[]或者[[]]的方法，直接用any()判断，注意一点all([])返回True
        m, n = len(matrix), len(matrix[0])
        return [matrix[i][j] for i, j in \
                sorted([(i, j) for i in range(m) for j in range(n)], \
                key=lambda x:(x[0]+x[1], x[(x[0]^x[1])&1^1]))]
# 代码解析：x[0]+x[1]的奇偶性和x[0]^x[1]奇偶性相同，此外判断奇偶的方法是n&1；最后因为和是奇数的时候要让[0]升序，偶数时候要让[1]升序，因此还要取反。
#1.判断和的奇偶性x[0]^x[1])&1，注意&的优先度高于^；然后取反x[0]^x[1])&1^1