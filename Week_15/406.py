# 参考 https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution
# 这题的逻辑是这样的，序号k只和比自己高或与自己等高的人数相关，而无视比自己矮的人；所以合理的排序方式是先拍个子高的，然后再让矮的插入进去，因为矮的不管怎么排都对高的人的k不产生影响。
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1])) # 让tuple中第一个元素从大到小排列，第二个元素从小到大排列
        ret = []
        for h, k in people:
            ret.insert(k, [h, k])
        return ret