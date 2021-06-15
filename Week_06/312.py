# 解法建议直接看视频 https://www.youtube.com/watch?v=IFNibRVgFBo
# 这题核心就先考虑爆破一个小范围的气球，能获得的最高分数是多少，这个范围逐渐扩大；然后第二层的思考是这个小范围的气球如何引爆的，
# 及如果k是这个小范围内的最后一个被引爆气球，那么k左边和右边先爆，范围总分数为左小范围+右小范围+k引爆分数，
# 初始情况为范围是1，单个气球引爆的分数。DP[i][j]的意义就是爆破范围[i, j]的气球能获得的最高分数。
class Solution:
    def maxCoins(self, nums: List[int]) -> int:  
        if not nums: return 0     
        nums = [1] + nums + [1]
        sz = len(nums)
        dp = [[None]*(sz-1) for _ in range(sz-1)]
        for l in range(1, sz-1): # 最外层的循环随着滑动窗口的长度从1变成整个nums长度
            for i in range(1, sz-l): # 第二层循环用于遍历滑动窗口左右边界；i为临时滑动窗口的左边界，j为临时滑动窗口的有边界
                if 0 == i: continue # 因为dp[0][:]与dp[:][0]会是dummy区域，直接跳过就可以了
                j = i + l - 1
                max_num = 0
                for k in range(i, j+1): # 第三层k作为最后一个被破的气球去遍历滑动窗口
                    left = 0 if k == i else dp[i][k-1]+0 # +0是为方便查找bug，查看DP表是否能正确填写
                    right = 0 if k == j else dp[k+1][j]+0
                    t = nums[i-1]*nums[k]*nums[j+1] + left + right
                    max_num = max(max_num, t)
                dp[i][j] = max_num
        return dp[1][-1]