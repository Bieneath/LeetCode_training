# https://leetcode.com/problems/subarray-product-less-than-k/discuss/?currentPage=1&orderBy=most_votes&query=
# 这已经是第二次栽在划窗计数上了！！！淦。比如[1, 2, 3]，它的所有子串为[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]，因此个数为3+2+1=6，也就是3~1累加。这个过程我们可以用le,ri两点的距离模拟得到相同的结果。一开始i=j=0, j-i+1=1;接着i=0,j=1,j-i+1=2;接着i=0,j=2,j-i+1=3;1+2+3=6
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = count = 0
        acc = 1
        for j, v in enumerate(nums):
            acc *= v
            while acc >= k and i <= j:
                acc /= nums[i]
                i += 1
            count += j - i + 1
        return count