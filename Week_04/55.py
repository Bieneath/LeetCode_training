# 基于贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        l = len(nums)
        i = 0
        while True:
            n = nums[i]
            max_dis = i + n
            if max_dis >= l - 1:
                return True
            pos = i
            for j in range(i+1, i+1+n):
                if j + nums[j] > max_dis:
                    pos, max_dis = j, j + nums[j]
            if pos == i: return False
            i = pos

# 基于类似加油站思路的O(n)算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for n in nums:
            if steps < 0: return False
            steps = max(steps, n)
            steps -= 1
        return True