# 这题思路很有意思，分为两种情况，1.如果n足够大，就像一个一个框一样，能把所有种类的任务都放在框里，那么框的个数就是
# 所有任务中数量最多的任务的个数。最后一个框，因为不一定满，所以要额外算一下，及有个数最多的任务种类有几种。
# 2.如果n不那么足够大，那么每个框不足以包含所有任务种类，此时就会产生“溢出”，那么这时候总体长度就是tasks的长度。
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        c = Counter(tasks)
        vs = c.values()
        max_v = max(vs)
        n_max_v = list(vs).count(max_v)
        return max(l, (max_v - 1) * (n + 1) + n_max_v)