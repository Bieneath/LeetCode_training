# 基本思路就是4个数字随机抽取2个进行四则运算，运算结果再和剩下的两个数字进行四则运算。
# 这里用到了一些python的方法，比如itertools.combinations或者itertools.permutations
import itertools
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(24 - nums[0]) < 1e-3 # 判断是否为24,这里不能用nums[0] == 24进行判断！
        for (i, x), (j, y) in itertools.combinations(enumerate(nums), 2):
            if x*y: # 当x或y为0时，防止分母为0的出现；同时用集合去重,减少搜索量
                temp = {x+y, x-y, y-x, x*y, x/y, y/x}
            else: 
                temp = {x+y, x-y, y-x, x*y}
            # 获得nums中除去x,y后剩余的数字组成列表
            rest = [z for k,z in enumerate(nums) if i!=k!=j]
            # for n in temp:
            #     if self.judgePoint24([n] + rest):
            #         return True
            # 将上面三行用python style的方法写
            if any(self.judgePoint24([n] + rest) for n in temp):
                return True
        return False