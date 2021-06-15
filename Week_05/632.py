import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hp = [(it[0], i, 0) for i, it in enumerate(nums)]
        heapq.heapify(hp)
        right = max([it[0] for it in nums])
        ret = [float('-inf'), float('inf')]
        while True:
            left, i, j = heapq.heappop(hp)
            if right - left < ret[1] - ret[0]:
                ret = [left, right]
            if j >= len(nums[i]) - 1:
                break
            new_v = nums[i][j+1]
            right = max(right, new_v)
            heapq.heappush(hp, (new_v, i, j+1))
        return ret