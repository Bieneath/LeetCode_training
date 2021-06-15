# 参考 https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).
# 使用API方法
from functools import cmp_to_key # 将cmp函数转化为key的方法
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums): return '0'
        def my_cmp(a, b): # 如果返回值<0，保持a, b的顺序，如果>0，则返回b, a的顺序
            return int(b + a) - int(a + b)
        s = sorted(map(str, nums), key=cmp_to_key(my_cmp))
        return ''.join(s)

from functools import cmp_to_key # 将cmp函数转化为key的方法
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums): return '0'
        def my_cmp(a, b): # 如果返回值<0，保持a, b的顺序，如果>0，则返回b, a的顺序
            return int(b + a) - int(a + b)
        s = sorted(map(str, nums), key=cmp_to_key(my_cmp))
        return ''.join(s)