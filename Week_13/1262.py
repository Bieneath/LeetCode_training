# DP表长度为3，DP表只保存能被1，2，3整除的最大和。
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0] # 因为要求能被3整除的数字，所以准备三个格子
        for n in nums:
            temp = dp.copy() # 这里的copy不能少，因为要保证遍历的是原来的dp，在循环体中，dp会被改变，所以提前留个备份。
            for it in dp:
                idx = (it + n) % 3
                temp[idx] = max(temp[idx], it + n)
            dp = temp
        return dp[0]