# 暴力算法，难点在各种api的灵活、熟悉的应用
from itertools import product
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ["%d:%02d"%(h, m) \
                for h, m in product(range(12), range(60)) \
                if (bin(h) + bin(m)).count('1') == turnedOn]