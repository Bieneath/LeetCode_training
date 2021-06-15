class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2: return 0
        count = cur = 0
        while True:
            val = nums[cur]
            right = cur + val # 当前节点cur下一步能够到的最远右边界
            if right >= l - 1:
                count += 1
                break
            for i, v in enumerate(nums[cur+1:cur+1+val], cur+1):
                if i + v > right:
                    right = i + v
                    next_pos = i
            cur = next_pos
            count += 1
        return count