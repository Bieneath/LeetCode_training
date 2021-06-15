# 这题想要从小到大排序！！！然后[a, b], a<b因此b一定是a的倍数，如果c是b的倍数，那么c一定也是a的倍数
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = {-1: []} # -1能被所有数整除，dp字典是数组末尾数字为key，数组为value
        for n in nums:
            dp[n] = max([v for k, v in dp.items() if n%k == 0], key=len) + [n]
        return max(dp.values(), key=len)

# from collections import defaultdict
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         dp = defaultdict(list)
#         dp[nums[0]].append(nums[0])
#         for n in nums[1:]:
#             temp = [n]
#             for v in dp:
#                 if n % v == 0:
#                     if len(dp[v]) > len(temp) - 1:
#                         temp = dp[v] + [n]
#             dp[n] = temp
#         return sorted(dp.values(), key=len)[-1]